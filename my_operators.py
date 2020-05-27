import my_primefac as pf

def _op_plus(x, y):
    return x + y


def _op_minus(x, y):
    return x - y


def _op_multiply(x, y, z=1):
    return x * y * z


def _n1p1(is_negative):
    # Turns an "is negative" bool-ish value
    # to either -1 or +1, as appropriate
    return -1 if is_negative else 1


def _op_divide(x, y):
    ax, ay = map(abs, (x, y))
    pfax, pfay = map(pf.prime_factorization, (ax, ay))
    if pfax is None or pfay is None:
        return ('/', x, y)
    pfq = pf.subtract(pfax, pfay)
    numerator, denominator = pf.realize(pfq)
    n1p1 = _n1p1((x < 0) != (y < 0))
    signed_numerator = n1p1 * numerator
    if denominator == 1:
        return signed_numerator
    return ('/', signed_numerator, denominator)


_OPLOOKUP = {
    '+': _op_plus,
    '-': _op_minus,
    '*': _op_multiply,
    '/': _op_divide,
}


def eval(opstr, *args):
    opfn = _OPLOOKUP[opstr]
    return opfn(*args)
