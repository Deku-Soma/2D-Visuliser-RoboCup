import pytest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from unittest.mock import patch
import os
from xvfbwrapper import Xvfb
from timesimple import Timer


class TestTimer:

    @classmethod
    def setUpClass(cls):
        if "DISPLAY" in os.environ:
            cls.win = tk.Tk()

    @classmethod
    def tearDownClass(cls):
        if cls.win is not None:
            cls.win.destroy()

    @pytest.mark.skipif("DISPLAY" not in os.environ, reason="Skipping GUI test in headless environment")
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
        assert self.timer.format_time() == "01:02:03"

    def test_start_timer(self):
        assert not self.timer.ticking
        self.timer.timer_play_pause()
        assert self.timer.ticking
        assert self.timer.play_pause_button["text"] == "⏸"
        self.timer.timer_play_pause()
        assert not self.timer.ticking
        assert self.timer.play_pause_button["text"] == "▶"

    def test_stop_timer(self):
        self.timer.timer_play_pause()
        assert self.timer.ticking
        self.timer.timer_play_pause()
        assert not self.timer.ticking

    def test_tick_timer(self):
        self.timer.time_step_slider_value.set(0)
        self.timer.ticking = True
        self.timer.timer_tick()
        assert self.timer.time_step.get() == 1
        assert self.timer.next_time_step.get() == 1

        self.timer.ticking = False
        self.timer.rewind = True
        self.timer.timer_tick()
        assert self.timer.time_step.get() == 0
        assert self.timer.next_time_step.get() == 1

    def test_rewind_timer(self):
        assert not self.timer.rewind
        self.timer.timer_rewind()
        assert self.timer.rewind
        assert self.timer.rewind_button["text"] == "⏭"
        self.timer.timer_rewind()
        assert not self.timer.rewind
        assert self.timer.rewind_button["text"] == "⏪"

    def test_speedup_timer(self):
        assert self.timer.speed_up.get() == 1
        self.timer.timer_speedup()
        assert self.timer.speed_up.get() == 2
        self.timer.timer_speedup()
        assert self.timer.speed_up.get() == 4

    def test_slowdown_timer(self):
        assert self.timer.speed_up.get() == 1
        self.timer.timer_speedup()
        self.timer.timer_slowdown()
        assert self.timer.speed_up.get() == 2
        self.timer.timer_slowdown()
        assert self.timer.speed_up.get() == 1


if __name__ == '__main__':
    pytest.main()
