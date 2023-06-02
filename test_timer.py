import unittest
import tkinter as tk
import timesimple as ts
import time
from xvfbwrapper import Xvfb


class TimerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vdisplay = Xvfb()
        cls.vdisplay.start()

    @classmethod
    def tearDownClass(cls):
        cls.vdisplay.stop()

    def test_play_pause(self):
        timer = ts.Timer(tk.Tk())

        self.assertFalse(timer.ticking)
        self.assertEqual("Play", timer.play_pause_button.cget("text"))

        timer.timer_play_pause()
        self.assertTrue(timer.ticking)
        self.assertEqual("Pause", timer.play_pause_button.cget("text"))

        timer.timer_play_pause()
        self.assertFalse(timer.ticking)
        self.assertEqual("Play", timer.play_pause_button.cget("text"))

    def test_rewind(self):
        timer = ts.Timer(tk.Tk())

        self.assertFalse(timer.rewind)
        self.assertEqual("Rewind", timer.rewind_button.cget("text"))

        timer.timer_rewind()
        self.assertTrue(timer.rewind)
        self.assertEqual("Forward", timer.rewind_button.cget("text"))

        timer.timer_rewind()
        self.assertFalse(timer.rewind)
        self.assertEqual("Rewind", timer.rewind_button.cget("text"))

    def test_speedup(self):
        timer = ts.Timer(tk.Tk())

        self.assertEqual(1, timer.speed_up)

        timer.timer_speedup()
        self.assertEqual(2, timer.speed_up)

    def test_slowdown(self):
        timer = ts.Timer(tk.Tk())

        timer.timer_slowdown()
        self.assertEqual(0.5, timer.speed_up)

    def test_tick(self):
        timer = ts.Timer(tk.Tk())

        timer.timer_tick()
        self.assertEqual(0, timer.time_step)
        self.assertEqual(0, timer.next_time_step)

        timer.timer_play_pause()
        timer.timer_tick()
        self.assertEqual(1, timer.time_step)
        self.assertEqual(2, timer.next_time_step)

        timer.speed_up = 2
        timer.time_step = 0
        timer.timer_tick()
        self.assertEqual(2, timer.time_step)
        self.assertEqual(4, timer.next_time_step)

        timer.speed_up = 1
        timer.rewind = True
        timer.time_step = 10
        timer.timer_tick()
        self.assertEqual(9, timer.time_step)
        self.assertEqual(8, timer.next_time_step)

        timer.speed_up = 1 / 2
        timer.rewind = False
        timer.time_step = 0

        start_time = time.time()
        timer.timer_tick()
        end_time = time.time() - start_time

        self.assertEqual(1, timer.time_step)
        self.assertEqual(2, timer.next_time_step)
        self.assertEqual(0.04, round(end_time, 2))

        timer.time_step = -1
        timer.ticking = True
        timer.rewind = True
        timer.speed_up = 1
        timer.timer_tick()
        self.assertEqual(0, timer.time_step)
        self.assertFalse(timer.ticking)
        self.assertFalse(timer.rewind)
        self.assertEqual(1, timer.speed_up)

        timer.time_step = 1
        timer.ticking = True
        timer.rewind = True
        timer.speed_up = 1
        timer.timer_tick()
        self.assertEqual(0, timer.time_step)
        self.assertFalse(timer.ticking)
        self.assertFalse(timer.rewind)
        self.assertEqual(1, timer.speed_up)

        timer.time_step = timer.max_ticks
        timer.ticking = True
        timer.speed_up = 5
        timer.timer_tick()
        self.assertEqual(timer.max_ticks, timer.time_step)
        self.assertFalse(timer.ticking)
        self.assertEqual(1, timer.speed_up)


if __name__ == '__main__':
    unittest.main()
