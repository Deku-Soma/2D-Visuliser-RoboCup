import tkinter as tk
import time


class Timer:
    # Set the duration of the game in seconds

    def __init__(self, master, max_ticks=100000, tick_rate=20):

        self.master = master  # This is the TK frame the buttons and slider will be stored in
        self.time_step = 0  # This stores what the current time step is
        self.next_time_step = 0  # This stores what the next time step is
        self.max_ticks = max_ticks  # This sets what are the total ticks the timer should run
        self.tick_rate = tick_rate  # This sets the tick rate of the timer

        # Speed up determines the tick speed, Ticking determines if the clock is running
        # Rewind determines if the clock is ticking backwards
        self.speed_up = 1
        self.ticking = False
        self.rewind = False
        self.gametime=0
        # Here is where we set up all the buttons
        self.play_pause_button = tk.Button(self.master, text="▶", command=self.timer_play_pause, font=("Arial", 11))
        self.play_pause_button.grid(row=2, column=0)  # Set column span to 2 for equal width
        self.tooltip_play_pause = Tooltip(self.play_pause_button, "Play/Pause")
        self.rewind_button = tk.Button(self.master, text="⏩", command=self.timer_rewind, font=("Arial", 11))
        self.rewind_button.grid(row=2, column=1)  # Set column span to 2 for equal width
        self.tooltip_rewind = Tooltip(self.rewind_button, "Rewind/Forward")
        self.speedup_button = tk.Button(self.master, text="⏩⏩", command=self.timer_speedup, font=("Arial", 11))
        self.speedup_button.grid(row=2, column=2)  # Set column span to 2 for equal width
        self.tooltip_speedup = Tooltip(self.speedup_button, "Speed Up")
        self.slowdown_button = tk.Button(self.master, text="⏪⏪", font=("Arial", 11))
        self.slowdown_button.grid(row=2, column=3)  # Set column span to 2 for equal width
        self.tooltip_slowdown = Tooltip(self.slowdown_button, "Slow Down")

        # Here is where the time slider is set up
        self.time_step_slider_value = tk.IntVar()
        self.time_step_slider = tk.Scale(from_=0, to=self.max_ticks, orient="horizontal",
                                         variable=self.time_step_slider_value, font=("Arial", 12),
                                         length=700)  # Adjust the length of the time slider here
        self.time_step_slider.grid(row=12, column=0, columnspan=2)

    def timer_play_pause(self):
        self.ticking = not self.ticking

        if self.ticking:
            self.play_pause_button.configure(text="⏸")
        else:
            self.play_pause_button.configure(text="▶")

    # This sets the clock to rewind mode
    def timer_rewind(self):
        self.rewind = not self.rewind

        if self.rewind:
            self.rewind_button.configure(text="⏭")
        else:
            self.rewind_button.configure(text="⏪")

    # This speeds up the tick rate of the clock
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

    # This formats the clock for the TKinter window display
    def format_time(self):
        total_seconds = self.gametime
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
