# encoding=utf8
# pylint: disable=anomalous-backslash-in-string
"""Implementation of Whitley function.

Date: February 2018

Authors: Grega Vrbančič and Lucija Brezočnik

License: MIT

Function: Whitley function

Input domain:
    The function can be defined on any input domain but it is usually
    evaluated on the hypercube x_i ∈ [-10.24, 10.24], for all i = 1, 2,..., D.

Global minimum:
    f(x*) = 0, at x* = (1,...,1)

LaTeX formats:
    Inline: $f(x_1 \cdots x_D) =
            \sum_{i=1}^D \sum_{j=1}^D (\frac{(100(x_i^2-x_j)^2 +
            (1-x_j)^2)^2}{4000} -cos(100(x_i^2-x_j)^2 + (1-x_j)^2)+1)$
    Equation: \begin{equation}f(x_1 \cdots x_D) =
              \sum_{i=1}^D \sum_{j=1}^D (\frac{(100(x_i^2-x_j)^2 +
              (1-x_j)^2)^2}{4000} -cos(100(x_i^2-x_j)^2 +
              (1-x_j)^2)+1) \end{equation}
    Domain: $-10.24 \leq x_i \leq 10.24$

Reference paper:
    Jamil, M., and Yang, X. S. (2013).
    A literature survey of benchmark functions for global optimisation problems.
    International Journal of Mathematical Modelling and Numerical Optimisation,
    4(2), 150-194.
"""

import math

__all__ = ['Whitley']


class Whitley(object):
    def __init__(self, Lower=-10.24, Upper=10.24):
        self.Lower = Lower
        self.Upper = Upper

    @classmethod
    def function(cls):
        def evaluate(D, sol):

            val = 0.0

            for i in range(D):
                for j in range(D):
                    temp = 100 * math.pow((math.pow(sol[i], 2) - sol[j]), 2) + math.pow(1 - sol[j], 2)
                    val += (float(math.pow(temp, 2)) / 4000.0) - math.cos(temp) + 1
                    
            return val

        return evaluate
