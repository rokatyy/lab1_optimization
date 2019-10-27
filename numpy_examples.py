import numpy as np
from math import sin, cos, exp
from scipy.optimize import fsolve
from sympy import Symbol, nsolve
import scipy.optimize as sopt
from scipy.optimize import minimize_scalar


def solve_equation_system(data):
    """
        This method gets equation coefs and free members and returns
        solving a system of linear equations using the Gauss method
        Args:
            data - coefs in csv file
        Returns:
            (array) - solving a system of linear equations
    """
    equation_coefs = [item[:-1] for item in data]
    equation_free_members = [item[-1] for item in data]

    a = np.array(equation_coefs)
    b = np.array(equation_free_members)
    return np.linalg.solve(a, b)





def solve_nonlinear_equation(A, B, C):
    def fun(x):
        return A * sin(B * x[0]) * cos(C * x[1])

    xx0 = np.array([0.])  # starting point
    rslt = sopt.leastsq(fun, xx0, full_output=True)
    print("The solution is {}".format(rslt[0]))


    # x = Symbol('x')
    # y = Symbol('y')
    # return nsolve([A * sin(B * x) * cos(C * y)], [x], [1, 1])


def minimization_by_golden_section(A, B, C):
    """
            This method gets coefficients of a given equation and returns
            minimum function by the golden ratio method
            Args:
                A, B, C  (int) - coefs of a equation
            Returns:
                (float) - minimum function
    """

    def f(x):
        return A * sin(B * x) * cos(C * x ** 2)

    return minimize_scalar(f, method='golden').x


#print(solve_equation_system(np.genfromtxt('input_equation.csv', delimiter=',')))
#print(solve_nonlinear_equation(4,7,1))
#print(minimization_by_golden_section(4,7,100))
