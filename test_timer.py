import unittest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from unittest.mock import patch
import os
from xvfbwrapper import Xvfb
from timesimple import Timer


class TestTimer(unittest.TestCase):

  win = None

@classmethod
def setUpClass(cls):
    if "DISPLAY" in os.environ:
        cls.win = tk.Tk()

@classmethod
def tearDownClass(cls):
    if cls.win is not None:
        cls.win.destroy()

@unittest.skipIf("DISPLAY" not in os.environ, "Skipping GUI test in headless environment")
def test_gui(self):
    if "DISPLAY" not in os.environ:
        # Headless environment, use xvfb
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

def setUp(self):
    self.root = tk.Tk()
    self.timer = Timer(self.root, max_ticks=100000, tick_rate=20)

def tearDown(self):
    self.root.destroy()

def test_format_time(self):
    self.timer.gametime = 3723
    self.assertEqual(self.timer.format_time(), "01:02:03")

def test_start_timer(self):
    self.assertFalse(self.timer.ticking)
    self.timer.timer_play_pause()
    self.assertTrue(self.timer.ticking)
    self.assertEqual(self.timer.play_pause_button["text"], "⏸")
    self.timer.timer_play_pause()
    self.assertFalse(self.timer.ticking)
    self.assertEqual(self.timer.play_pause_button["text"], "▶")

def test_stop_timer(self):
    self.timer.timer_play_pause()
    self.assertTrue(self.timer.ticking)
    self.timer.timer_play_pause()
    self.assertFalse(self.timer.ticking)

def test_tick_timer(self):
    self.timer.time_step_slider_value.set(0)
    self.timer.ticking = True
    self.timer.timer_tick()
    self.assertEqual(self.timer.time_step, 1)
    self.assertEqual(self.timer.next_time_step, 1)

    self.timer.ticking = False
    self.timer.rewind = True
    self.timer.timer_tick()
    self.assertEqual(self.timer.time_step, 1)
    self.assertEqual(self.timer.next_time_step, 1)

def test_rewind_timer(self):
    self.assertFalse(self.timer.rewind)
    self.timer.timer_rewind()
    self.assertTrue(self.timer.rewind)
    self.assertEqual(self.timer.rewind_button["text"], "⏭")
    self.timer.timer_rewind()
    self.assertFalse(self.timer.rewind)
    self.assertEqual(self.timer.rewind_button["text"], "⏪")

def test_speedup_timer(self):
    self.assertEqual(self.timer.speed_up, 1)
    self.timer.timer_speedup()
    self.assertEqual(self.timer.speed_up, 2)
    self.timer.timer_speedup()
    self.assertEqual(self.timer.speed_up, 4)

def test_slowdown_timer(self):
    self.assertEqual(self.timer.speed_up, 1)
    self.timer.timer_speedup()
    self.timer.timer_slowdown()
    self.assertEqual(self.timer.speed_up, 2)
    self.timer.timer_slowdown()
    self.assertEqual(self.timer.speed_up, 1)



if __name__ == '__main__':
    unittest.main()















'''import unittest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from unittest.mock import patch
import os
from xvfbwrapper import Xvfb

from timesimple import Timer


class TestTimer(unittest.TestCase):

    win = None

    @classmethod
    def setUpClass(cls):
        if "DISPLAY" in os.environ:
            cls.win = tk.Tk()

    @classmethod
    def tearDownClass(cls):
        if cls.win is not None:
            cls.win.destroy()

    @unittest.skipIf("DISPLAY" not in os.environ, "Skipping GUI test in headless environment")
    def test_gui(self):
        if "DISPLAY" not in os.environ:
            # Headless environment, use xvfb
            
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

    # Rest of your test methods...


if __name__ == '__main__':
    unittest.main()'''