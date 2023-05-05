import unittest
import tkinter as tk
from timer import Timer

class TestTimer(unittest.TestCase):
    def test_timer(self):
        root = tk.Tk()
        timer = Timer(root)
        
        # Test initial time remaining
        self.assertEqual(timer.time_step, 90 * 60) #90 minutes
        
        # Test timer_tick method
        timer.timer_tick()
        self.assertEqual(timer.format_time(timer.time_step), "01:29:59")
        
        # Test stop_timer method
        timer.stop_timer()
        self.assertIsNone(timer.master.after(1000, timer.timer_tick))
        
if __name__ == '__main__':
    unittest.main()
