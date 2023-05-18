import unittest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from unittest.mock import patch
import os
import xvfbwrapper

from timefunctions import Timer


class TestTimer(unittest.TestCase):

    win = tk.Tk()

    @unittest.skipIf("DISPLAY" not in os.environ, "Skipping GUI test in headless environment")
    def test_gui(self):
        if "DISPLAY" not in os.environ:
            # Headless environment, use xvfb
            from xvfbwrapper import Xvfb
            with Xvfb() as xvfb:
                self.test_format_time()
                self.test_start_timer()
                self.test_stop_timer()
                self.test_tick_timer()
                self.test_rewind_timer()
                self.test_speedup_timer()
                self.test_slowdown_timer()
        else:
            # GUI test code goes here
            self.test_format_time()
            self.test_start_timer()
            self.test_stop_timer()
            self.test_tick_timer()
            self.test_rewind_timer()
            self.test_speedup_timer()
            self.test_slowdown_timer()


    def test_format_time(self):
        timer = Timer(self.win)

        timer.time_step = 60
        self.assertEqual(timer.format_time(), '00:01:00')

        timer.time_step = 3600
        self.assertEqual(timer.format_time(), '01:00:00')

        timer.time_step = 3661
        self.assertEqual(timer.format_time(), '01:01:01')

    def test_start_timer(self):
        timer = Timer(self.win)

        timer.start_timer()

        self.assertEqual(1, timer.speed_up)
        self.assertTrue(timer.ticking)

    def test_stop_timer(self):
        timer = Timer(self.win)

        timer.stop_timer()

        self.assertEqual(1, timer.speed_up)
        self.assertFalse(timer.ticking)

    def test_tick_timer(self):
        timer = Timer(self.win)

        timer.start_timer()

        timer.tick()

        self.assertEqual(1, timer.time_step)


    def test_rewind_timer(self):
        timer = Timer(self.win)

        timer.start_timer()
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

        timer.start_timer()
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

        timer.start_timer()
        timer.slowdown_timer()
        self.assertEqual(0.5, timer.speed_up)

        timer.speed_up = 2
        timer.slowdown_timer()
        self.assertEqual(1, timer.speed_up)



if __name__ == '__main__':
    unittest.main()
