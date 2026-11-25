import unittest

from src.queue_summary import count_active


class QueueTest(unittest.TestCase):
    def test_reopened(self):
        self.assertEqual(count_active(['reopened', 'closed']), 1)
