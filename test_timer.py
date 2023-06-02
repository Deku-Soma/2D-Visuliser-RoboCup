<<<<<<< HEAD
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

    # Rest of your test methods...


if __name__ == '__main__':
    unittest.main()
=======
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

    # Rest of your test methods...


if __name__ == '__main__':
    unittest.main()
>>>>>>> 791b50dd4ae03f25693058e1c63cadd1f6f49188
