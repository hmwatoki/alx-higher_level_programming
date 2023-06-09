#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list[list[int or float]]): A matrix to be divided.
        div (int or float): The divisor to divide the matrix elements by.

    Returns:
        new_matrix
    """

    check_matrix(matrix)
    check_same_row_size(matrix)
    check_div(div)
    new_matrix = div_matrix(matrix, div)
    return new_matrix


def check_matrix(matrix):
    """
    Check if the input matrix is a list of lists of integers or floats.

    Args:
        matrix (list[list[int or float]]): A matrix to be checked.

    Raises:
        TypeError: if the input matrix is not a list of lists of integers or floats.
    """

    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(
            isinstance(element, (int, float)) for element in row
        ) for row in matrix
    ):
        raise TypeError("Matrix must be a list of lists of integers or floats")


def check_same_row_size(matrix):
    """
    Check if each row of the input matrix has the same size.

    Args:
        matrix (list[list[int or float]]): A matrix to be checked.

    Raises:
        TypeError: if any row of the input matrix has a different size than the others.
    """

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")


def check_div(div):
    """
    Check if the `div` parameter is a number and not 0.

    Args:
        div (int or float): The divisor to be checked.

    Raises:
        TypeError: if `div` is not a number
        ZeroDivisionError: if `div` is 0
    """

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


def div_matrix(matrix, div):
    """
    Divide all elements of a matrix by a given divisor and round to two decimal places.

    Args:
        matrix (list[list[int or float]]): A matrix to be divided.
        div (int or float): The divisor to divide the matrix elements by.

    Returns:
        A new matrix where each element is divided by the divisor and rounded to two decimal places.
    """

    rows = len(matrix)
    cols = len(matrix[0])
    return [[round(matrix[i][j] / div, 2) for j in range(cols)] for i in range(rows)]
