import my_discriminant
import my_quadratic_roots
import my_html

def _condense_steps(steps):  # remove no-ops
    last_body = None
    new_steps = []
    for step in steps:
        explanation, body = step
        if body == last_body:
            continue
        new_steps.append((explanation, body))
        last_body = body
    return new_steps

def write_html_file_for_disc_and_qroots(a, b, c):
    dsteps = my_discriminant.calc(a, b, c)
    disc_steps = _condense_steps(dsteps)
    last_disc_step = disc_steps[-1]
    body_of_last_disc_step = last_disc_step[1]
    disc = body_of_last_disc_step
    steps_for_roots = {}
    for plmi in ('+', '-'):
        rsteps = my_quadratic_roots.calc(a, b, disc, plmi)
        steps_for_roots[plmi] = _condense_steps(rsteps)
    #
    name = 'a={} b={} c={}'.format(a, b, c)
    path = 'out/{}.html'.format(name)
    file_title = name
    calcs = (disc_steps, steps_for_roots['+'], steps_for_roots['-'])
    calc_titles = (
            'calculating discriminant with a={}, b={}, c={}'.format(a, b, c),
            'calculating {} root with a={}, b={}, disc={}'.format('+', a, b, disc),
            'calculating {} root with a={}, b={}, disc={}'.format('-', a, b, disc))
    my_html.write_to_html(path, file_title, calcs, calc_titles)
