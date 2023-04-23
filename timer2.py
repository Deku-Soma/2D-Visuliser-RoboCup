import tkinter as tk

# Set the duration of the game in seconds
GAME_DURATION = 90 * 60 #or (20 * 60) for the match to end in 20 minutes

class Timer:
    def __init__(self, master):
        self.master = master
        self.remaining = GAME_DURATION
        self.timer_label = tk.Label(master, text=self.format_time(self.remaining))
        self.timer_label.pack()
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack()
    
    def start_timer(self):
        self.timer_tick()
    
    def stop_timer(self):
        self.master.after_cancel(self.timer)
    
    def timer_tick(self):
        self.remaining -= 1
        self.timer_label.configure(text=self.format_time(self.remaining))
        if self.remaining <= 0:
            self.timer_label.configure(text="Game over!")
        else:
            self.timer = self.master.after(1000, self.timer_tick)
    
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

root = tk.Tk()
timer = Timer(root)
root.mainloop()
