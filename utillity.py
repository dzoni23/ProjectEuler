from math import floor, sqrt
from time import time
from functools import reduce
from operator import mul


def timer(func):
   def func_wrapper(*args):
       s = time()
       r = func(*args)
       e = time()
       return r, e-s
   return func_wrapper


def is_prime(num):
    for candidate in range(2, floor(sqrt(num)) + 1, 1):
        if num % candidate == 0:
            return False

    return True


def next_prime(p):
    if p == 2: return 3

    while True:
        p += 2
        if is_prime(p): return p


def is_palindrom_str(num):
    str_num = str(num)
    num_len = len(str_num)

    if num_len % 2 == 0:
        for i in range((num_len // 2)):
            if str_num[i] == str_num[num_len - 1]:
                i += 1
                num_len -= 1
            else:
                return False

        return True
    else:
        for i in range((num_len - 1) // 2):
            if str_num[i] == str_num[num_len-1]:
                i += 1
                num_len -= 1
            else:
                return False

        return True


def is_palindrome(num):
    """
    Complexity: O(d) , d = digit_number of num
    """
    d = 0
    num_c = num
    while num_c != 0:
        num_c //= 10
        d += 1

    num_tmp = num
    while d != 0:
        if num_tmp // 10 == 0:
            return True

        start = num_tmp // pow(10, d - 1)
        end = num_tmp % 10
        if start != end:
            return False
        num_tmp -= start * pow(10, d - 1)
        num_tmp //= 10
        d -= 2

    return True


def divisible_up_to(num, k):
    for i in range(1, k + 1):
        if not num % i == 0:
            return False

    return True


def sum_to_n(num):
    return (num * (num + 1)) // 2


def sum_to_n_2(num):
    return int((num**3 / 3) + (num**2 / 2) + (num / 6))


def is_pitagorean(a, b, c):
    return a**2 + b**2 == c**2


def check_start(mat, i, j):
    right, left, up, down = 0, 0, 0, 0
    dig_down_right, dig_up_left = 0, 0
    dig_up_right, dig_down_left = 0, 0

    if j+3 <= 19:
        right = reduce(mul, [mat[i][j+k] for k in range(4)])

    if j-3 >= 0:
        left = reduce(mul, [mat[i][j-k] for k in range(4)])

    if i+3 <= 19:
        down = reduce(mul, [mat[i+k][j] for k in range(4)])

    if i-3 >= 0:
        up = reduce(mul, [mat[i-k][j] for k in range(4)])

    if i+3 <= 19 and j+3 <= 19:
        dig_down_right = reduce(mul, [mat[i+k][j+k] for k in range(4)])

    if i - 3 >= 0 and j - 3 >= 0:
        dig_up_left = reduce(mul, [mat[i-k][j-k] for k in range(4)])

    if i-3 >= 0 and j+3 <=19:
        dig_up_right = reduce(mul, [mat[i-k][j+k] for k in range(4)])

    if i + 3 <= 19 and j - 3 >= 0:
        dig_down_left = reduce(mul, [mat[i+k][j-k] for k in range(4)])

    return max(right, left, up, down, dig_down_right, dig_up_left, dig_up_right, dig_down_left)


def form_triangular_num(i):
    return (i * (i + 1)) // 2


def num_divisors(num):
    divs = [i for i in range(1, num + 1) if num % i == 0]

    return divs, len(divs)


def num_divisors2(num):
    divs = list()

    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divs.append(i)
            if i is not num // i:
                divs.append(num // i)

    return divs, len(divs)








