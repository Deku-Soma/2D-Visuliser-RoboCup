from tkinter import Tk, Canvas, NW, Button
import time

class Timer:
    def __init__(self, master):
        self.master = master
        self.remaining = 20 * 60  # 20 minutes in seconds
        self.paused = False
        self.speedup = False
        self.start_time = None
        self.pause_start = None
        self.pause_time = 0

    def start_timer(self):
        self.start_time = time.monotonic()
        self.run_timer()

    def run_timer(self):
        if self.paused:
            self.master.after(100, self.run_timer)
            return

        elapsed = time.monotonic() - self.start_time - self.pause_time
        self.remaining = max(0, int((20 * 60) - elapsed))
        if self.speedup:
            self.remaining //= 2
        mins = self.remaining // 60
        secs = self.remaining % 60
        self.master.title(f"Time remaining: {mins:02}:{secs:02}")
        if self.remaining > 0:
            self.master.after(100, self.run_timer)

    def pause_timer(self):
        self.paused = True
        self.pause_start = time.monotonic()

    def unpause_timer(self):
        self.paused = False
        self.pause_time += time.monotonic() - self.pause_start
        self.run_timer()

    def toggle_speedup(self):
        self.speedup = not self.speedup

    def rewind_timer(self):
        if self.remaining > 10:
            self.remaining -= 10
        else:
            self.remaining = 0
        self.run_timer()

    def fast_forward_timer(self):
        self.remaining += 10
        self.run_timer()

   
win = Tk()
timer = Timer(win)
timer.start_timer()

# Pause the timer
timer.pause_timer()

# Unpause the timer
timer.unpause_timer()

# Toggle speedup mode
timer.toggle_speedup()

# Rewind the timer by 10 seconds
timer.rewind_timer()

# Fast forward the timer by 10 seconds
timer.fast_forward_timer()

win.mainloop()
