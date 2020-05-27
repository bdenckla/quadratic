import my_operators
import my_primefac as pf


def calc(a, b, c):
    bsq = '*', b, b
    fac = '*', 4, a, c
    sub = '-', bsq, fac
    sub2 = '-', my_operators.eval(*bsq), my_operators.eval(*fac)
    sub3 = my_operators.eval(*sub2)
    return (
        ('substitute abc', ('sqrt', sub)),
        ('eval products inside', ('sqrt', sub2)),
        ('eval subtraction inside', ('sqrt', sub3)),
        ('evict squares', _move_squares_out(sub3)),
    )


def _sqrt_sep(inside):
    pfai = pf.prime_factorization(abs(inside))
    if pfai is None:
        return 1, inside
    new_outside, new_inside = {}, {}
    for prime, power in pfai.items():
        new_outside[prime] = power // 2
        new_inside[prime] = power % 2
    n1p1 = _n1p1(inside < 0)
    return pf.realize_int(new_outside), n1p1 * pf.realize_int(new_inside)


def _n1p1(is_negative):
    # Turns an "is negative" bool-ish value
    # to either -1 or +1, as appropriate
    return -1 if is_negative else 1


def _move_squares_out(inside):
    outside, new_inside = _sqrt_sep(inside)
    if outside == 1:
        return ('sqrt', inside)
    if new_inside == 1:
        return outside
    return ('*', outside, ('sqrt', new_inside))
