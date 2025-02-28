import unittest
from app import time_difference

class TestTimeDifference(unittest.TestCase):
    def test_time_difference(self):
        self.assertEqual(time_difference("15:00", "14:45"), -15)
        self.assertEqual(time_difference("15:00", "15:05"), 5)
        self.assertEqual(time_difference("15:00", "15:00"), 0)
        self.assertEqual(time_difference("15:00", "14:40"), -20)

if __name__ == "__main__":
    unittest.main()
