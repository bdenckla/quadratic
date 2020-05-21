import html

def write_to_html(path, title, calcs, calc_titles):
    html_el = _html_el2(title, _render_calcs(calcs, calc_titles))
    _write_html_to_file(html_el, path)


def _write_html_to_file(html_el, path):
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('<!doctype html>\n')
        fh.write(_el_to_str(html_el))


def _html_el2(title_text, body_contents, lang='en', charset='utf-8'):
    meta = {'tag': 'meta', 'noclose': True}
    title = {'tag': 'title', 'contents': (title_text,)}
    _head = {'tag': 'head', 'contents': (meta, title)}
    _body = {'tag': 'body', 'contents': body_contents}
    return _html_el1({'lang': lang}, (_head, _body))


def _html_el1(attr, contents):
    return {'tag': 'html', 'attr': attr, 'contents': contents}


def _el_to_str(el):
    if isinstance(el, str):
        return html.escape(el)
    elcont = el.get('contents', tuple())
    if isinstance(elcont, dict) and elcont.get('tag'):
        contents = _el_to_str(elcont)
    else:
        contents = ''.join(map(_el_to_str, elcont))
    lb2 = el.get('lb2', '\n')
    fields = {
        'tag_name': el['tag'],
        'attr': _attr_str(el.get('attr')),
        'contents': contents,
        'close': '</{}>{}'.format(el['tag'], lb2),
        'lb1': el.get('lb1', '\n'),
    }
    return '<{tag_name}{attr}>{lb1}{contents}{close}'.format(**fields)


def _attr_str(attr_dict):
    if not attr_dict:
        return ''
    return ' ' + ' '.join(map(_kv_str, attr_dict.items()))


def _kv_str(kv):
    return '{}="{}"'.format(kv[0], html.escape(kv[1], quote=True))


def _para(contents):
    return {'tag': 'p', 'contents': contents, 'lb1': ''}


def _tr(contents):
    return {'tag': 'tr', 'contents': contents, 'lb1': ''}


def _td(contents):
    return {'tag': 'td', 'contents': contents, 'lb1': '', 'lb2': ''}


def _table(contents):
    return {'tag': 'table', 'contents': contents}


def _div(contents):
    return {'tag': 'div', 'contents': contents}


def _pre(contents):
    return {'tag': 'pre', 'contents': contents}


def _math(contents):
    return {'tag': 'math', 'contents': contents}


def _msqrt(contents):
    return {'tag': 'msqrt', 'contents': contents}


def _mn(contents):
    return {'tag': 'mn', 'contents': contents}


def _mo(contents):
    return {'tag': 'mo', 'contents': contents}


def _mfrac(contents):
    return {'tag': 'mfrac', 'contents': contents}


def _mrow(contents):
    return {'tag': 'mrow', 'contents': contents}


def _render_calcs(calcs, calc_titles):
    return tuple(map(_render_calc, calcs, calc_titles))


def _render_calc(calc_steps, calc_title):
    para_of_title = _para(calc_title)
    table_of_steps = _table(tuple(map(_render_step, calc_steps)))
    return _div((para_of_title, table_of_steps))


def _render_steps(steps):
    return _table(tuple(map(_render_step, steps)))


def _render_step(step):
    explanation, math_expr = step
    inside = _render_inside(math_expr)
    return _tr((_td(_math(inside)), _td(explanation)))


def _render_inside(expr):
    if isinstance(expr, int):
        return (_mn((str(expr),)),)
    first = expr[0]
    if first == 'sqrt':
        return (_msqrt(_render_inside(expr[1])),)
    if first in ('+', '-', '*'):
        if len(expr) == 3:
            return _render_inside(expr[1]) + (_mo((first,)),) + _render_inside(expr[2])
        if len(expr) == 4:
            return _render_inside(expr[1]) + (_mo((first,)),) + _render_inside(expr[2]) + (_mo((first,)),) + _render_inside(expr[3])
    if first == '/':
        return (_mfrac((_mrow(_render_inside(expr[1])), _mrow(_render_inside(expr[2])))),)
    return (_pre((str(expr),)),)
