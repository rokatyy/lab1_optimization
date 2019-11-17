import numpy as np


class Vector:
    def __init__(self, elements):
        self.base_elements = elements


class Matrix(Vector):
    def __init__(self, elements):
        super().__init__(elements[0])  # pass the first row
        self.elements = elements


class EquationSystem(Matrix):
    def __init__(self, elements, solutions):
        super().__init__(elements)  # pass coefficients matrix
        self.solutions = solutions

    def solve(self):
        return np.linalg.solve(self.elements, self.solutions)
