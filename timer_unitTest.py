import unittest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from unittest.mock import patch

from timefunctions import Timer


class TestTimer(unittest.TestCase):

    win = tk.Tk()

    def test_format_time(self):
        timer = Timer(self.win)

        timer.time_step = 60
        self.assertEqual(timer.format_time(), '00:01:00')

        timer.time_step = 3600
        self.assertEqual(timer.format_time(), '01:00:00')

        timer.time_step = 3661
        self.assertEqual(timer.format_time(), '01:01:01')

    def test_play_pause_timer(self):
        timer = Timer(self.win)

        timer.play_pause()

        self.assertEqual(1, timer.speed_up)
        self.assertTrue(timer.ticking)

        timer.play_pause()

        self.assertFalse(timer.ticking)

    def test_tick_timer(self):
        timer = Timer(self.win)

        timer.play_pause()

        timer.tick()

        self.assertEqual(1, timer.time_step)


    def test_rewind_timer(self):
        timer = Timer(self.win)

        timer.play_pause()
        timer.tick()
        timer.rewind_timer()

        timer.tick()
        self.assertTrue(timer.rewind)
        self.assertEqual(0, timer.time_step)

        timer.tick()
        self.assertEqual(0, timer.time_step)

        timer.rewind_timer()
        self.assertFalse(timer.rewind)

    def test_speedup_timer(self):
        timer = Timer(self.win)

        timer.play_pause()
        timer.speedup_timer()
        self.assertEqual(2, timer.speed_up)

        timer.speed_up = 0.25
        timer.speedup_timer()
        self.assertEqual(0.5, timer.speed_up)

        timer.speed_up = 4
        timer.speedup_timer()
        self.assertEqual(4, timer.speed_up)

    def test_slowdown_timer(self):
        timer = Timer(self.win)

        timer.play_pause()
        timer.slowdown_timer()
        self.assertEqual(0.5, timer.speed_up)

        timer.speed_up = 2
        timer.slowdown_timer()
        self.assertEqual(1, timer.speed_up)

    def test_skip_forward_timer(self):
        timer = Timer(self.win)

        timer.skip_forward()

        self.assertEqual(30, timer.time_step)

    def test_skip_backwards_timer(self):
        timer = Timer(self.win)

        timer.time_step = 31
        timer.skip_backwards()
        self.assertEqual(1, timer.time_step)

        timer.skip_backwards()
        self.assertEqual(0, timer.time_step)


if __name__ == '__main__':
    unittest.main()
