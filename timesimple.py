import tkinter as tk
import time


class Timer:
    def __init__(self, master, max_ticks=100000, tick_rate=20):
        self.master = master
        self.time_step = 0
        self.next_time_step = 0
        self.max_ticks = max_ticks
        self.tick_rate = tick_rate
        self.speed_up = 1
        self.ticking = False
        self.rewind = False

        self.play_pause_button = tk.Button(self.master, text="▶", command=self.timer_play_pause, font=("Arial", 11))
        self.play_pause_button.grid(row=8, column=0, columnspan=2)
        self.tooltip_play_pause = Tooltip(self.play_pause_button, "Play/Pause")
        self.rewind_button = tk.Button(self.master, text="⏩", command=self.timer_rewind, font=("Arial", 11))
        self.rewind_button.grid(row=10, column=0, columnspan=2)
        self.tooltip_rewind = Tooltip(self.rewind_button, "Rewind/Forward")
        self.speedup_button = tk.Button(self.master, text="⏩⏩", command=self.timer_speedup, font=("Arial", 11))
        self.speedup_button.grid(row=11, column=0, columnspan=2)
        self.tooltip_speedup = Tooltip(self.speedup_button, "Speed Up")
        self.slowdown_button = tk.Button(self.master, text="⏪⏪", font=("Arial", 11))
        self.slowdown_button.grid(row=9, column=0, columnspan=2)
        self.tooltip_slowdown = Tooltip(self.slowdown_button, "Slow Down")

        self.time_step_slider_value = tk.IntVar()
        self.time_step_slider = tk.Scale(from_=0, to=self.max_ticks, orient="horizontal",
                                         variable=self.time_step_slider_value, font=("Arial", 12),
                                         length=700, showvalue=False, command=self.update_time_label)
        self.time_step_slider.grid(row=12, column=0, columnspan=2)

        # Create a StringVar to store the time value as a string
        self.time_value = tk.StringVar()

        # Create a label to display the time value
        self.time_label = tk.Label(self.master, textvariable=self.time_value, font=("Arial", 12))
        self.time_label.grid(row=7, column=0, columnspan=2)

        # Hide the time label initially
        self.time_label.grid_remove()

        self.update_time_label(0)

    def timer_play_pause(self):
        self.ticking = not self.ticking

        if self.ticking:
            self.play_pause_button.configure(text="⏸")
        else:
            self.play_pause_button.configure(text="▶")

    def timer_rewind(self):
        self.rewind = not self.rewind

        if self.rewind:
            self.rewind_button.configure(text="⏭")
        else:
            self.rewind_button.configure(text="⏪")

    def timer_speedup(self):
        self.speed_up *= 2

    def timer_slowdown(self):
        self.speed_up /= 2

    def timer_tick(self):
        self.time_step = self.time_step_slider_value.get()

        if self.speed_up >= 1:
            self.time_step += self.ticking * self.speed_up * (-1) ** self.rewind
            self.next_time_step = self.time_step + self.ticking * self.speed_up * (-1) ** self.rewind
        else:
            self.time_step += self.ticking * (-1) ** self.rewind
            self.next_time_step = self.time_step + self.ticking * (-1) ** self.rewind

        time.sleep(0.02 / self.speed_up)

        if self.time_step < 0 or self.next_time_step < 0:
            self.time_step = 0
            self.ticking = False
            self.rewind = False
            self.speed_up = 1

        if self.time_step > self.max_ticks:
            self.time_step = self.max_ticks
            self.ticking = False
            self.speed_up = 1

        self.time_step_slider_value.set(self.time_step)

        # Update the time value in the StringVar
        self.time_value.set(self.format_time())

    def update_time_label(self, value):
        self.time_label.configure(text=self.format_time())

    def format_time(self):
        total_seconds = self.time_step / self.tick_rate
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", borderwidth=1,
                         font=("Arial", 10))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

