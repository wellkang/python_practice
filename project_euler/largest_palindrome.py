# -*- coding: utf-8 -*-

"""
"""


def is_palindrome(num):
    r = num
    nums = []
    while num > 0:
        n = num % 10
        num /= 10
        nums.append(str(n))
    return True if int(''.join(nums)) == r else False


def get_largest_palindrom():
    largest_palindrom = 0
    for i in range(99, 1000):
        for j in range(99, 1000):
            if is_palindrome(i * j) and i * j > largest_palindrom:
                largest_palindrom = i * j
    return largest_palindrom


if __name__ == '__main__':
    print get_largest_palindrom()