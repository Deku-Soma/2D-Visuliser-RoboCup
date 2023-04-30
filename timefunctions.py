import tkinter as tk


class Timer:
    # Set the duration of the game in seconds

    GAME_DURATION = 0  # or (20 * 60) for the match to end in 20 minutes

    def __init__(self, master, print_timer):
        self.master = master
        self.remaining = self.GAME_DURATION
        self.timer_label = tk.Label(master, text=self.format_time(self.GAME_DURATION))
        self.timer_label.pack()
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(master, text="Pause", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.rewind_button = tk.Button(master, text="Rewind", command=self.rewind_timer)
        self.rewind_button.pack(side=tk.LEFT, padx=5)
        self.speedup_button = tk.Button(master, text="Speed Up", command=self.speedup_timer)
        self.speedup_button.pack(side=tk.LEFT, padx=5)

        self.speed_up = 1
        self.ticking = False
        self.rewind = False

    def start_timer(self):
        self.speed_up = 1
        self.rewind = False

        if not self.ticking:
            self.ticking = True
            self.timer_tick()

    def stop_timer(self):
        # Pause function
        self.speed_up = 1
        self.rewind = False

        if self.ticking:
            self.master.after_cancel(self.timer)
            self.ticking = False


    def rewind_timer(self):
        self.rewind = True

        #self.timer_label.configure(text=self.format_time(self.remaining))

    def speedup_timer(self):

        self.speed_up += 1

        '''self.remaining -= 60 # speed up by one minute
        self.timer_label.configure(text=self.format_time(self.remaining))'''

    def timer_tick(self):
        self.remaining += 1 * (-1) ** self.rewind

        self.timer_label.configure(text=self.format_time(self.remaining))
        if self.remaining <= 0:
            self.timer_label.configure(text="Game over!")
        else:
            # ensures that a 90 minute game is completed in 20 minutes
            self.timer = self.master.after(int(1000/self.speed_up), self.timer_tick)  # increment timer by a factor of 4.5 (90/20)

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


root = tk.Tk()
root.title("Soccer Game Timer")
# Create the Timer object inside the window

# timer.start()

class PrintTime:

    def __init__(self, master):
        self.master = master
        self.time = 0

        self.print_time_label = tk.Label(master)
        self.print_time_label.pack()

    def print(self, time):
        self.time = time
        print(self.time)
# Start the main event loop


print_time = PrintTime(root)

timer = Timer(root, print_time)

root.mainloop()

