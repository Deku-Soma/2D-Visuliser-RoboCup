import threading
import tkinter as tk
import time

class Timer:
    # Set the duration of the game in seconds

    GAME_DURATION = 0  # or (20 * 60) for the match to end in 20 minutes

    def __init__(self, tps=33, max_ticks=0):

        self.time_step = 0 # This stores what is the current time step
        self.tps = tps #Stores how many tick happen per second
        self.max_ticks = max_ticks # This sets what are the total ticks the timer should run

        # Speed up is determines the tick speed, Ticking determines if the clock is running
        # Rewind determines if the clock is ticking backwards
        self.speed_up = 1
        self.ticking = False
        self.rewind = 0

    # This gets the clock to start moving forward
    def start_timer(self):
        self.ticking=True

    #This pasues the clock
    def stop_timer(self):
        self.ticking = False
        self.speed_up=1

    # This sets the clock to rewind mode
    def rewind_timer(self):
        self.rewind = 1
        self.speed_up=1

    # This speeds up the tick rate of the clock
    def speedup_timer(self):
        self.speed_up += 1
        '''self.remaining -= 60 # speed up by one minute
        self.timer_label.configure(text=self.format_time(self.remaining))'''

    # This is where the clock updates, If rewind = True it will run backwards, speed_up will determine
    # the clock tick rate

    def tick(self):
        self.timer_label.configure(text=self.format_time())

    # This formats the clock for the TKinter window display
    def format_time(self):
        seconds, ticks =  divmod(self.time_step, self.tps)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

