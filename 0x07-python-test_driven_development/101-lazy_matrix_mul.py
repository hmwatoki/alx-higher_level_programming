#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using.

    Args:
        m_a (List[List[int or float]]): 1st matrix to be multiplied.
        m_b (List[List[int or float]]): 2nd matrix to be multiplied.

    Returns:
        List[List[int or float]]: Resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list of lists, or if one element of those list of lists is not an integer or a float, or if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size).
        ValueError: If m_a or m_b is empty (it means: = [] or = [[]]), or if m_a and m_b can not be multiplied.

    Examples:
        >>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        array([[19, 22],
               [43, 50]])

        >>> lazy_matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
        array([[ 58,  64],
               [139, 154]])

        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
        Traceback (most recent call last):
            ...
        ValueError: m_a and m_b can't be multiplied

        >>> lazy_matrix_mul([[1, 2], [3, 'a']], [[4, 5], [6, 7]])
        Traceback (most recent call last):
            ...
        TypeError: m_a should contain only integers or floats or m_b should contain only integers or floats

        >>> lazy_matrix_mul([], [])
        Traceback (most recent call last):
            ...
        ValueError: m_a can't be empty or m_b can't be empty

        >>> lazy_matrix_mul([1, 2], [3, 4])
        Traceback (most recent call last):
            ...
        TypeError: m_a must be a list or m_b must be a list

        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
        Traceback (most recent call last):
            ...
        TypeError: each row of m_a must be of the same size or each row of m_b must be of the same size
    """

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not isinstance(m_a, np.ndarray) or not isinstance(m_b, np.ndarray):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a or m_b is not a list of lists")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)

    return result.tolist()
