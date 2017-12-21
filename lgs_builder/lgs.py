#!/usr/bin/env python3

from numpy import matrix
from numpy.linalg import det
from random import randint

import tex2pix

def generate_matrix(matrix_list=[]):
    data_template = "{} {} {}; {} {} {}; {} {} {}"
    data = data_template.format(*[randint(-10, 10) for _ in range(9)])
    if det(matrix(data)) == 0:
        return generate_matrix(matrix_list)
    return matrix(data)


def generate_solution():
    data_template = '{}; {}; {}'
    data_values = [randint(-5,5) for _ in range(3)]
    if data_values[0] == 0:
        return generate_solution()
    data = data_template.format(*data_values)
    return matrix(data)


def build_exam():
    M = generate_matrix()
    x = generate_solution()
    v = M*x
    template = "({}) \\cdot a + ({}) \\cdot b + ({}) \\cdot c &= {} \\\\"
    lines = []
    for i in range(3):
        lines.append(template.format(*M.tolist()[i],*v.tolist()[i]))
    return '\n'.join(lines), [i[0] for i in x.tolist()]


def create_texcode():
    exam, solution = build_exam()
    texcode = '''
\\documentclass[preview]{standalone}
\\usepackage{amsmath}
\\pagestyle{empty}
\\begin{document}

\\begin{align*}
''' + exam + '''
\\end{align*}
\\end{document}
'''
    return texcode, solution


def build_png():
    t,s=create_texcode()
    r = tex2pix.Renderer(t)
    filename = "L " + " ".join(map(str, s)) + '.png'
    print(filename)
    r.mkpng(filename)

build_png()
