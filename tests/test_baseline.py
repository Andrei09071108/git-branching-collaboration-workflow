import unittest

from src.queue_summary import count_active


class QueueTest(unittest.TestCase):
    def test_baseline(self):
        self.assertEqual(count_active(['open', 'closed', 'open']), 2)
