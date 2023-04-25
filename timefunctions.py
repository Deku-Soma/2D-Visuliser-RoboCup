import time
import tkinter as tk

class Timer:
    def __init__(self, master):
        # Initialize variables
        self._start = 0
        self._elapsed = 0
        self._paused_time = 0
        self._paused = False
        self._speed = 1.0

        # Create button and pack it
        self._pause_button = tk.Button(master, text="Pause", command=self.pause)
        self._pause_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create second button and pack it
        self._resume_button = tk.Button(master, text="Resume", command=self.resume)
        self._resume_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create third button and pack it
        self._speedup_button = tk.Button(master, text="Speedup", command=self.speedup)
        self._speedup_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create fourth button and pack it
        self._rewind_button = tk.Button(master, text="Rewind", command=self.rewind)
        self._rewind_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Create label to display timer
        self._timer_label = tk.Label(master, text="0:00")
        self._timer_label.pack(side=tk.TOP, fill=tk.X)

        # Keep updating the timer display
        self._update()

    def start(self):
        # Start the timer
        self._start = time.monotonic()

    def stop(self):
        # Stop the timer and reset variables
        self._start = 0
        self._elapsed = 0
        self._paused_time = 0
        self._paused = False
        self._speed = 1.0

    def pause(self):
    # Pause the timer
        if not self._paused:
            self._paused_time = time.monotonic()  # Record the time the timer was paused
            self._paused = True  # Set the paused flag to True

    def resume(self):
    # Resume the timer
        if self._paused:
            self._start += time.monotonic() - self._paused_time  # Update the start time with the time the timer was paused
            self._paused_time = 0  # Reset the paused time to zero
            self._paused = False  # Set the paused flag to False

    def speedup(self):
        # Rewind the timer by 10 seconds
        self._start -= 30

    def rewind(self):
        # Double the speed of the timer
        self._speed *= 2

    def slowdown(self):
        # Halve the speed of the timer
        self._speed /= 2

    def _update(self):
        # Update the timer display
        if self._start is not None:
            elapsed_time = time.monotonic() - self._start
            if not self._paused:
                elapsed_time /= self._speed
            else:
                self._paused_time += 1
            elapsed_time = min(elapsed_time, 20*60) # limit elapsed time to 20 minutes
            minutes, seconds = divmod(elapsed_time, 60)
            self._timer_label.config(text=f"{int(minutes)}:{int(seconds):02d}")
        self._timer_label.after(1000, self._update) # update every second

# Create the main window
root = tk.Tk()
root.title("Soccer Game Timer")
# Create the Timer object inside the window
timer = Timer(root)
timer.start()

# Start the main event loop
root.mainloop()

