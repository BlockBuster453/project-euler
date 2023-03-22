from math import isqrt
import math
import os


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


if __name__ == '__main__':
    target_number = 600851475143
    reduced_target = isqrt(600851475143)

    for i in range(reduced_target, 3, -1):
        print("checks primality of " + str(i))
        if i % 2 == 0:
            continue
        if is_prime(i) and target_number % i == 0:
            print(str(i) + " is the largest prime factor")
            break
