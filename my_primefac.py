import collections


def prime_factorization(n):
    if n <= 0:
        return None
    primes = _primes_leq(n)
    if primes is None:
        return None
    counter = collections.Counter()
    r = n
    for candidate in primes:
        while r > 1 and r % candidate == 0:
            counter[candidate] += 1
            r = r // candidate
    return counter


_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def _primes_leq(n):
    if n > _PRIMES[-1]:
        return None
    return [p for p in _PRIMES if p <= n]


def _quick_test():
    for i in range(30):
        print(i, prime_factorization(i))


if __name__ == "__main__":
    _quick_test()
