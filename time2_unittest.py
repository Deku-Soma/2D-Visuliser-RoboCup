import unittest
import tkinter as tk
import time
from timefunctions import Timer


class TestTimer(unittest.TestCase):
    win = tk.Tk()

    def test_start(self):
        timer = Timer(self.win)
        timer.start_timer()

        self.assertEqual(1, timer.speed_up)
        self.assertFalse(timer.rewind)

    def test_stop(self):
        timer = Timer(self.win)
        timer.stop_timer()

        timer.tick()

        self.assertEqual(0, timer.time_step)
        self.assertEqual(1, timer.speed_up)
        self.assertFalse(timer.rewind)
        self.assertFalse(timer.ticking)

    def test_tick(self):
        timer = Timer(self.win)
        timer.start_timer()
        timer.tick()

        self.assertEqual(1, timer.time_step)

    def test_rewind(self):
        timer = Timer(self.win)

        timer.tick()
        timer.rewind_timer()
        timer.tick()

        self.assertEqual(0, timer.time_step)
        self.assertTrue(timer.rewind)

    def test_speedup(self):
        timer = Timer(self.win)

        timer.start_timer()
        timer.speedup_timer()

        start_time = time.time()
        timer.tick()
        duration = time.time() - start_time

        self.assertEqual(2, timer.speed_up)
        self.assertAlmostEqual(timer.tick_duration / timer.speed_up, round(duration, 1))


if __name__ == '__main__':
    unittest.main()
