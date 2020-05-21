import my_operators

def calc(a, b, disc, plmi):
    numerator = plmi, -b, disc
    denom = '*', 2, a
    denom2 = my_operators.eval(*denom)
    numerator2 = _eval_if_intargs(*numerator)
    frac = _eval_if_intargs('/', numerator2, denom2)
    return (
        ('substitute a, b, disc', ('/', numerator, denom)),
        ('eval_denominator', ('/', numerator, denom2)),
        ('eval_numerator', ('/', numerator2, denom2)),
        ('eval_frac', frac),
    )

def _eval_if_intargs(opstr, x, y):
    if isinstance(x, int) and isinstance(y, int):
        return my_operators.eval(opstr, x, y)
    return (opstr, x, y)
