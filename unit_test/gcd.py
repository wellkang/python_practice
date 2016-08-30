# -*- coding: utf-8 -*-

"""
"""
def get_num(start, num, step):
    n = start
    while n < num:
        yield n
        n += step

def get_largest_prime_factor(min_factor, num):
    if min_factor == 2:
        if num % 2 == 0:
            if num == 2:
                return 2
            else:
                return get_largest_prime_factor(2, num/2)
        else:
            return get_largest_prime_factor(3, num)
    for i in get_num(min_factor, num / 2 + 1, 2):
        if num % i == 0:
            return get_largest_prime_factor(i, num / i)
    return num


if __name__ == '__main__':\
    print get_largest_prime_factor(2, 600851475143)
