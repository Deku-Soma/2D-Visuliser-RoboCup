import tkinter as tk

# Set the duration of the game in seconds
GAME_DURATION = 90 * 60 #or (20 * 60) for the match to end in 20 minutes

class Timer:
    def __init__(self, master):
        self.master = master
        self.remaining = 0
        self.increment = 1
        self.timer_label = tk.Label(master, text=self.format_time(self.remaining))
        self.timer_label.pack()
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(master, text="Pause", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.rewind_button = tk.Button(master, text="Rewind", command=self.rewind_timer)
        self.rewind_button.pack(side=tk.LEFT, padx=5)
        self.fastforward_button = tk.Button(master, text="Fast Forward", command=self.fastforward_timer)
        self.fastforward_button.pack(side=tk.LEFT, padx=5)
        self.speedup_button = tk.Button(master, text="Speed Up", command=self.speedup_timer)
        self.speedup_button.pack(side=tk.LEFT, padx=5)
    
    def start_timer(self):
        self.timer_tick()
    
    def stop_timer(self): 
        # Pause function
        self.master.after_cancel(self.timer)
    
    def rewind_timer(self):
        self.remaining -= 60 # subtract one minute
        self.timer_label.configure(text=self.format_time(self.remaining))
    
    def fastforward_timer(self):
        self.remaining += self.increment
        self.timer_label.configure(text=self.format_time(self.remaining))
    
    def speedup_timer(self):
        self.increment *= 2
        self.timer_label.configure(text=self.format_time(self.increment))
    
    def timer_tick(self):
        self.remaining += 1
        self.timer_label.configure(text=self.format_time(self.remaining))
        if self.remaining >= GAME_DURATION:
            self.timer_label.configure(text="Timer has ended!")
        else:
            # ensures that a 90 minute game is completed in 20 minutes
            self.timer = self.master.after(250, self.timer_tick) # increment timer by a factor of 4.5 (90/20)
    
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


root = tk.Tk()
root.title("Soccer Game Timer")
# Create the Timer object inside the window
timer = Timer(root)
#timer.start()

# Start the main event loop
root.mainloop()
