def _op_plus(x, y):
    return x + y


def _op_minus(x, y):
    return x - y


def _op_multiply(x, y, z=1):
    return x * y * z


def _op_divide(x, y):
    return x // y if x % y == 0 else ('/', x, y)


_OPLOOKUP = {
    '+': _op_plus,
    '-': _op_minus,
    '*': _op_multiply,
    '/': _op_divide,
}


def eval(opstr, *args):
    opfn = _OPLOOKUP[opstr]
    return opfn(*args)
