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


def realize(pf):
    numerator = 1
    denominator = 1
    for prime, power in pf.items():
        if power >= 0:
            numerator *= prime ** power
        else:
            denominator *= prime ** (-power)
    return numerator, denominator


def realize_int(pf):
    n, d = realize(pf)
    assert d == 1
    return n


def subtract(pf1, pf2):
    result = collections.Counter(pf1)
    result.subtract(pf2)
    return result


_PRIMES = [
      2,     3,     5,     7,    11,    13,    17,    19,    23,    29,
     31,    37,    41,    43,    47,    53,    59,    61,    67,    71,
     73,    79,    83,    89,    97,   101,   103,   107,   109,   113,
    127,   131,   137,   139,   149,   151,   157,   163,   167,   173,
    179,   181,   191,   193,   197,   199,   211,   223,   227,   229,
    233,   239,   241,   251,   257,   263,   269,   271,   277,   281,
    283,   293,   307,   311,   313,   317,   331,   337,   347,   349,
    353,   359,   367,   373,   379,   383,   389,   397,   401,   409,
    419,   421,   431,   433,   439,   443,   449,   457,   461,   463,
    467,   479,   487,   491,   499,   503,   509,   521,   523,   541,
    547,   557,   563,   569,   571,   577,   587,   593,   599,   601,
    607,   613,   617,   619,   631,   641,   643,   647,   653,   659,
    661,   673,   677,   683,   691,   701,   709,   719,   727,   733,
    739,   743,   751,   757,   761,   769,   773,   787,   797,   809,
    811,   821,   823,   827,   829,   839,   853,   857,   859,   863,
    877,   881,   883,   887,   907,   911,   919,   929,   937,   941,
    947,   953,   967,   971,   977,   983,   991,   997
]


def _primes_leq(n):
    if n > _PRIMES[-1]:
        return None
    return [p for p in _PRIMES if p <= n]


def _quick_test():
    for i in range(30):
        print(i, prime_factorization(i))


if __name__ == "__main__":
    _quick_test()
