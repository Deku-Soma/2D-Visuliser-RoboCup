import tkinter as tk
import time

class Timer:
    # Set the duration of the game in seconds

    GAME_DURATION = 0  # or (20 * 60) for the match to end in 20 minutes

    def __init__(self, master, game_duration=1000000000):

        # Create buttons and added it to a TKinter Label
        self.master = master
        self.time_step = 0
        self.game_duration = game_duration


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
            self.master.after_cancel(self.timer)
            self.ticking = False

    # This sets the clock to rewind mode
    def rewind_timer(self):
        self.rewind = True

    # This speeds up the tick rate of the clock
    def speedup_timer(self):

        self.speed_up += 1

        '''self.remaining -= 60 # speed up by one minute
        self.timer_label.configure(text=self.format_time(self.remaining))'''

    # This is where the clock updates, If rewind = True it will run backwards, speed_up will determine
    # the clock tick rate
    def timer_tick(self):
        self.time_step += 1 * (-1) ** self.rewind

        self.timer_label.configure(text=self.format_time(self.time_step))
        if self.time_step <= 0: # This needs to be altered in the future
            self.timer_label.configure(text="Game over!")
        else:
            # This determines the rate at which the clock ticks, 1000 = 1 sec
            self.timer = self.master.after(int(1000/self.speed_up), self.timer_tick)

    def tick(self):
        self.time_step += self.ticking * (-1) ** self.rewind
        
        time.sleep(self.tick_duration / self.speed_up)

    # This formats the clock for the TKinter window display
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


