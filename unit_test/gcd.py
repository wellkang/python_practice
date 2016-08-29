# -*- coding: utf-8 -*-

"""
"""


class GCD:

    def __init__(self):
        pass

    def gcd(self, num1, num2):
        min = (num1 < num2) and num1 or num2
        gcd_num = 1
        for i in range(1, min+1):
            a = num1 % i
            b = num2 % i
            if a == 0 and b == 0:
                gcd_num = i
        return gcd_num
