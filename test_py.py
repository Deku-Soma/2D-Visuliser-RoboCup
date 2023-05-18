import unittest
import Visualiser
from xvfbwrapper import Xvfb
import os


class TestStringMethods(unittest.TestCase):

    @unittest.skipIf("DISPLAY" not in os.environ, "Skipping GUI test in headless environment")
    def test_gui(self):
        if "DISPLAY" not in os.environ:
            # Headless environment, use xvfb
            
            with Xvfb() as xvfb:
                self.test_function()
                self.test_upper()
                self.test_isupper()
                self.test_split()
                
        else:
            # GUI test code goes here
            self.test_function()
            self.test_upper()
            self.test_isupper()
            self.test_split()
            

    def test_function(self):
        self.assertEqual(Visualiser.function(1,2),3)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()