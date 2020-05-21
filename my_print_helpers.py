import my_discriminant
import my_quadratic_roots
import my_html

def _print_steps(steps):
    last_body = None
    for step in steps:
        explanation, body = step
        infix_body = _reorder_to_infix(body)
        if infix_body != last_body:
            print('{} ({})'.format(infix_body, explanation))
        last_body = infix_body

def _reorder_to_infix(expr):
    if isinstance(expr, int):
        return expr
    op, *rest = expr
    rerest = tuple(map(_reorder_to_infix, rest))
    if op in ('+', '-', '*', '/') and len(rerest) == 2:
        return rerest[0], op, rerest[1]
    if op in ('*') and len(rest) == 3:
        return rerest[0], op, rerest[1], op, rerest[2]
    return (op,) + rerest

def print_steps_for_disc_and_qroots(a, b, c):
    disc_steps = my_discriminant.calc(a, b, c)
    name = 'a={} b={} c={}'.format(a, b, c)
    path = 'out/{}.html'.format(name)
    title = name
    my_html.write_to_html(path, title, disc_steps)
    print('calculating discriminant with a={}, b={}, c={}'.format(a, b, c))
    _print_steps(disc_steps)
    last_disc_step = disc_steps[-1]
    body_of_last_disc_step = last_disc_step[1]
    disc = body_of_last_disc_step
    print()
    print('calculating root with a={}, b={}, disc={}, plmi={}'.format(a, b, disc, '+'))
    _print_steps(my_quadratic_roots.calc(a, b, disc, '+'))
    print()
    print('calculating root with a={}, b={}, disc={}, plmi={}'.format(a, b, disc, '-'))
    _print_steps(my_quadratic_roots.calc(a, b, disc, '-'))
