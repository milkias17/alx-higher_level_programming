#!/usr/bin/python3
"""
    Module with function to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Calculates the sum of two numbers

    :param matrix: List[int] | List[float]
    :param div: int | float

    :return: List[int] | List[float]: new matrix where every element is divided by div

    :raises: TypeError: when matrix isn't a matrix of integers/floats or when div isn't a number
             ZeroDivisionError: when div is zero.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = None
    new_mat = []
    for row in matrix:
        tmp = []
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if size is None:
            size = len(row)
        else:
            if len(row) != size:
                raise TypeError("Each row of the matrix must have the same size")

        for el in row:
            if type(el) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            tmp.append(round(el / div, 2))

        new_mat.append(tmp)

    return new_mat
