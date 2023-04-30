import unittest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from unittest.mock import patch

from timefunctions import Timer


class TestTimer(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.timer = Timer(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_format_time(self):
        self.assertEqual(self.timer.format_time(60), '00:01:00')
        self.assertEqual(self.timer.format_time(3600), '01:00:00')
        self.assertEqual(self.timer.format_time(3661), '01:01:01')

    def test_start_timer(self):
        with patch.object(self.timer, 'timer_tick') as mock_timer_tick:
            self.timer.start_timer()
            mock_timer_tick.assert_called()

    def test_stop_timer(self):
        self.timer.stop_timer()

    def test_rewind_timer(self):
        initial_remaining = self.timer.remaining
        self.timer.rewind_timer()
        self.assertEqual(self.timer.remaining, initial_remaining + 60)

    def test_speedup_timer(self):
        initial_remaining = self.timer.remaining
        self.timer.speedup_timer()
        self.assertEqual(self.timer.remaining, initial_remaining - 60)

    def test_timer_tick(self):
        initial_remaining = self.timer.remaining
        self.timer.timer_tick()
        self.assertEqual(self.timer.remaining, initial_remaining - 1)

    def test_game_over(self):
        self.timer.remaining = 0
        self.timer.timer_tick()
        self.assertEqual(self.timer.timer_label['text'], 'Game over!')

if __name__ == '__main__':
    unittest.main()
