import unittest
from color import Color, get_closest_color

# Make sure that the program recognizes hues greater than violet as red.
class test_red_hi(unittest.TestCase):
    def test(self):
        self.assertEqual(get_closest_color(340), "RED")


class test_spectrum(unittest.TestCase):
    def test(self):
        for c in Color.keys():
            val = Color[c][0]
            if c == "RED_HI":
                self.assertEqual(get_closest_color(val), "RED")
            else:
                self.assertEqual(get_closest_color(val), c)

