# -*- coding: utf-8 -*-

"""
"""
import datetime
import math


def get_prime_factor(num):
    i = 2
    factors = []
    while i <= math.sqrt(num):
        if num % i == 0:
            factors.append(i)
            num /= i
            continue
        i += 1
    factors.append(num)
    return factors


def get_smallest_multiple(num):
    factors = []
    result = 1
    for i in range(2, num + 1):
        max_count_i = 0
        for j in range(i, num + 1):
            factors_j = get_prime_factor(j)
            if factors_j.count(i) > max_count_i:
                max_count_i = factors_j.count(i)
        factors.append(max_count_i)
    print factors
    for i in range(len(factors)):
        if factors[i]:
            result *= (i+2) ** factors[i]
    return result


def get_sum_square_difference(num):
    sum_square = 0
    sum = 0
    for i in range(num + 1):
        sum_square += i * i
    for i in range(num + 1):
        sum += i
    square_sum = sum * sum
    return sum_square - square_sum


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    n = 3
    while n <= math.sqrt(num):
        if num % n == 0:
            return False
        n += 2
    return True


def get_nst_prime(num):
    n = 1
    for i in range(num):
        while True:
            n += 1
            if is_prime(n):
                break
    return n


def get_largest_product(str, n):
    largest_product = 0
    for i in range(len(str) - n):
        product = 1
        for j in range(n):
            product *= int(str[i+j])
        if product > largest_product:
            largest_product = product
    return largest_product


def pythagorean():
    for i in range(1, 334):
        for j in range(333, 500):
            k = 1000 - i - j
            if i * i + j * j == k * k:
                return i, j, k


def get_sum_of_prime(num):
    sum_of_prime = 2
    n = 0
    i = 3
    # for i in range(3, num + 1, 2):
    while i < num + 1:
        if is_prime(i):
            n += 1
            sum_of_prime += i
        i += 2
    return sum_of_prime, n


def get_divisible_number():
    triangle_number = 0
    c_n = 0
    while True:
        c_n += 1
        triangle_number += c_n
        factors = get_prime_factor(triangle_number)
        fac_set = set(factors)
        fac_re = 0
        n = len(factors)
        for f in fac_set:
            fac_re += factors.count(f) - 1
        divisors = n * (n + 1) / 2 - fac_re + 1
        print divisors, triangle_number
        if divisors >= 500:
            return triangle_number


if __name__ == '__main__':
    print get_divisible_number()
    # print get_prime_factor(43770268128)
