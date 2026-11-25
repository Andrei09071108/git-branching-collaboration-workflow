import unittest

from src.queue_summary import count_active


class QueueTest(unittest.TestCase):
    def test_waiting(self):
        self.assertEqual(count_active(['waiting', 'closed']), 1)
