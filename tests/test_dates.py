# -*- encoding: utf-8 -*-


import unittest

from dateconv import *


class TestAll(unittest.TestCase):
    def test_times(self):
        human_time = '2015-01-01 18:21:26'
        datetime_time = datetime.datetime(2015, 1, 1, 18, 21, 26)
        unix_time = 1420114886

        self.assertEqual(d2u(datetime_time), unix_time)
        self.assertEqual(d2h(datetime_time), human_time)
        self.assertEqual(h2u(human_time), unix_time)
        self.assertEqual(h2d(human_time), datetime_time)
        self.assertEqual(u2d(unix_time), datetime_time)
        self.assertEqual(u2h(unix_time), human_time)


if __name__ == '__main__':
    unittest.main()
