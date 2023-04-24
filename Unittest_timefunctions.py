import unittest
import time

class TestSoccerTimer(unittest.TestCase):
    def test_timer(self):
        timer = SoccerTimer()
        timer.start_timer()
        time.sleep(1)  # Wait for 1 second
        timer.pause_timer()
        pause_time = timer.pause_time
        self.assertTrue(pause_time > 0)
        timer.unpause_timer()
        time.sleep(1)  # Wait for 1 second
        self.assertTrue(timer.elapsed > 0)
        timer.toggle_speedup()
        time.sleep(1)  # Wait for 1 second
        self.assertTrue(timer.elapsed > 120)
        timer.rewind_timer()
        self.assertTrue(timer.elapsed < 120)
        timer.fast_forward_timer()
        self.assertTrue(timer.elapsed > 120)
