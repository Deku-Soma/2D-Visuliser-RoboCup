import time
import sys
sys.setrecursionlimit(6000)
class SoccerTimer:
    def __init__(self):
        self.elapsed = 0
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
            time.sleep(0.1)
            self.run_timer()
            return

        self.elapsed = time.monotonic() - self.start_time - self.pause_time
        if self.speedup:
            self.elapsed *= 2
        if self.elapsed >= 5400:  # stop the timer if it exceeds 90 minutes
            return
        mins = int(self.elapsed // 60)
        secs = int(self.elapsed % 60)
        print(f"Time elapsed: {mins:02}:{secs:02}")
        time.sleep(0.1)
        self.run_timer()

    def pause_timer(self):
        self.paused = True
        self.pause_start = time.monotonic()

    def unpause_timer(self):
        self.paused = False
        self.pause_time += time.monotonic() - self.pause_start

    def toggle_speedup(self):
        self.speedup = not self.speedup

    def rewind_timer(self):
        if self.elapsed > 10:
            self.elapsed -= 10
        else:
            self.elapsed = 0

    def fast_forward_timer(self):
        self.elapsed += 10


# Create a new soccer timer
timer = SoccerTimer()

# Start the timer
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
