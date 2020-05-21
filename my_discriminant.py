import my_operators


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

_SQRT_SEP = {
    8: (2, 2),  # 8 = 2*sqrt(2)
    16: (4, 1),  # 8 = 4*sqrt(1)
    36: (6, 1),
}


def _move_squares_out(inside):
    outside, new_inside = _SQRT_SEP.get(inside, (1, inside))
    if outside == 1:
        return ('sqrt', inside)
    if new_inside == 1:
        return outside
    return ('*', outside, ('sqrt', new_inside))
