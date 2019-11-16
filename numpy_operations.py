import numpy as np
from math import sin, cos, exp
import scipy.optimize as optimize
from scipy.optimize import minimize_scalar


def solve_equation_system(data):
    """
    This method gets equation coefficients and free members and returns
    solving a system of linear equations using the Gauss method
    Args:
        data (numpy csv file object)- coefficients in csv file
    Returns:
        (array) - solving a system of linear equations
    """
    equation_coefs = [item[:-1] for item in data]
    equation_free_members = [item[-1] for item in data]
    a = np.array(equation_coefs)
    b = np.array(equation_free_members)
    return np.linalg.solve(a, b)


def solve_nonlinear_equation(A, B, C, start=0, end=0):
    """
    Solving a nonlinear equation `A * np.sin(B * x) * np.cos(C * x)`.
    Coefficients A, B and C specifies by a user.
    Additionally, a range for solutions can be passed (`start` and `end`).

    Args:
        A, B, C  (int) - coefficients of an equation
        start  (int) - a starting point of range
        end  (int) - an ending point of range
    Returns:
        (array) - solutions for the specified range
    """

    step = (end - start) / 100

    def fun(x):
        return A * np.sin(B * x) * np.cos(C * x)

    result = optimize.diagbroyden(fun, np.arange(start, end, step))

    return list(
        filter(
            lambda x: start <= x <= end,
            np.unique(np.around(result, decimals=5))
        )
    )


def minimization_by_golden_section(A, B, C):
    """
    This method gets coefficients of a given equation and returns
    minimum function by the golden ratio method
    Args:
        A, B, C  (int) - coefficients of a equation
    Returns:
        (float) - minimum function
    """

    def f(x):
        return A * sin(B * x) * cos(C * x ** 2)

    return minimize_scalar(f, method='golden').x
