"""
This is a module for code that can be used project-wide.
For now we only need functions for working with sympy Series so I'm putting them
all in here.
Might need refactoring as the book changes.
"""

from functools import partial
import numpy as np
from sympy.abc import x
from sympy.core.add import Add


def _eval_series_at_point(series: Add, x_val: float) -> float:
    """
    Evaluates the truncated series "series" at point "x_val."
    """
    series = series.subs(x, x_val)
    return float(series.evalf())

def get_pointwise_values(series: Add, domain: np.array) -> np.array:
    """
    Returns an array containing pointwise values of truncated series "series"
    for all values in the domain "domain".
    """
    eval_at_point = partial(_eval_series_at_point, series)
    series_vectorized = np.vectorize(eval_at_point)
    pointwise_values = series_vectorized(domain)
    return pointwise_values
