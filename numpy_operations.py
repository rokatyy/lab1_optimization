import numpy as np
from math import sin, cos, exp
import scipy.optimize as sopt
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


def solve_nonlinear_equation(A, B, C):
    """
            This method gets coefficients of a given equation and returns solution
            Args:
                A, B, C (int) - coefficients of a equation
            Returns:
                result (scipy library result) - solution of nonlinear equation
    """

    def fun(x):
        return A * sin(B * x[0]) * cos(C * x[1])

    xx0 = np.array([0.])  # starting point
    result = sopt.leastsq(fun, xx0, full_output=True)
    print("The solution is {}".format(result[0]))


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
