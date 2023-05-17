import threading
import tkinter as tk
import time

class Timer:
    # Set the duration of the game in seconds

    GAME_DURATION = 0  # or (20 * 60) for the match to end in 20 minutes

    def __init__(self, master, tps=1, max_ticks=0):

        self.master = master
        self.time_step = 0 # This stores what is the current time step
        self.tps = tps #Stores how many tick happen per second
        self.max_ticks = max_ticks # This sets what are the total ticks the timer should run

        # Create buttons and added it to a TKinter Label

        self.timer_label = tk.Label(master, text=self.format_time())
        self.timer_label.pack()
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(master, text="Pause", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.rewind_button = tk.Button(master, text="Rewind", command=self.rewind_timer)
        self.rewind_button.pack(side=tk.LEFT, padx=5)
        self.speedup_button = tk.Button(master, text="Speed Up", command=self.speedup_timer)
        self.speedup_button.pack(side=tk.LEFT, padx=5)

        # Speed up is determines the tick speed, Ticking determines if the clock is running
        # Rewind determines if the clock is ticking backwards
        self.speed_up = 1
        self.tick_duration = 1
        self.ticking = False
        self.rewind = False

    # This gets the clock to start moving forward
    def start_timer(self):
        self.speed_up = 1
        self.rewind = False

        if not self.ticking:
            self.ticking = True
            #self.timer_tick()

    #This pasues the clock
    def stop_timer(self):
        # Pause function
        self.speed_up = 1
        self.rewind = False

        if self.ticking:
            #self.master.after_cancel(self.timer)
            self.ticking = False

    # This sets the clock to rewind mode
    def rewind_timer(self):
        self.rewind = not self.rewind

    # This speeds up the tick rate of the clock
    def speedup_timer(self):

        self.speed_up += 1

        '''self.remaining -= 60 # speed up by one minute
        self.timer_label.configure(text=self.format_time(self.remaining))'''

    # This is where the clock updates, If rewind = True it will run backwards, speed_up will determine
    # the clock tick rate

    def tick(self):
        self.time_step += self.ticking * (-1) ** self.rewind

        if self.time_step < 0:
            self.time_step = 0

        self.timer_label.configure(text=self.format_time())

    # This formats the clock for the TKinter window display
    def format_time(self):
        seconds, ticks =  divmod(self.time_step, self.tps)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


