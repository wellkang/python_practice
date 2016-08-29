# -*- coding: utf-8 -*-

"""
"""
import unittest
from unit_test.gcd import GCD


class TestGCD(unittest.TestCase):

    def test_init(self):
        pass

    def test_gcd(self):
        gcd = GCD()
        num = gcd.gcd(32, 56)
        self.assertEquals(num, 8)


if __name__ == '__main__':
    unittest.main()
