import tkinter as tk
import json
import time

class Timer:
    def __init__(self, data):
        # Create a counter variable
        self.counter = -1
        self.counter_array = []

        # Loop through the rows and save counter value to array
        for row in data:
            self.counter += 1
            self.counter_array.append(self.counter)

        # Define variables for tracking time and current position
        self.start_time = None
        self.current_position = None
        self.time_step = 1  # in seconds
        self.paused = False
        self.speedup = False
        self.data = data

    # Define the update_position function
    def update_position(self):
        if not self.paused:
            if self.start_time is None:
                self.start_time = time.time()
                self.current_position = 0
            else:
                elapsed_time = time.time() - self.start_time
                #if speedup is True, the elapsed time is multiplied by 2 to simulate a 2x speedup.
                if self.speedup:
                    elapsed_time *= 2
                target_position = int(elapsed_time / self.time_step)
                if target_position != self.current_position:
                    self.current_position = min(target_position, len(self.counter_array) - 1)
                    # Code to update current position in data goes here
                    data_at_position = self.data[self.counter_array[self.current_position]]
                    # Code to update display with data_at_position goes here

    # Pause function
    def pause(self):
        self.paused = not self.paused

    # Resume function
    def resume(self):
        self.paused = False

    # Rewind function with while loop: stops when pause is selected or counter <= 0
    def rewind(self):
        while not self.paused and self.counter > 0:
            self.counter -= 1
        # Get the data at the current position
            data_at_position = self.data[self.counter_array[self.counter]]
        # Code to update display with the data_at_position goes here
            time.sleep(self.time_step)  # Wait for time_step seconds before moving to previous position


    # Get data at current position
    def get_data_at_current_position(self):
        position = self.counter_array[self.current_position]
        return self.data[position]

    # Define the step_back function
    def step_back(self):
        if self.counter > 0:
            self.counter -= 1
            data_at_position = self.data[self.counter_array[self.counter]]
            # Code to update display with data_at_position goes here

    # Define the step_forward function
    def step_forward(self):
        if self.counter < len(self.counter_array) - 1:
            self.counter += 1
            data_at_position = self.data[self.counter_array[self.counter]]
            # Code to update display with data_at_position goes here
    
    # Define the speedup function
    def toggle_speedup(self):
        self.speedup = not self.speedup


