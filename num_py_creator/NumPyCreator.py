from typing import Iterator
from numpy.random import rand
from numpy import float64, int64
from numpy import asarray, fromiter, identity, full_like


class NumPyCreator(object):

    def __init__(self):
        ...

    def from_list(self, lst: list, dtype=None):
        """
        Convert  a list into a numpy array object
        @param: self: object
        @param: lst: a list
        return: a numpy array object
        """
        if type(lst) != list:
            return None
        try:
            npatmp = asarray(lst, dtype=object)
            npatmp.shape[1]
        except IndexError:
            return None
        return asarray(lst, dtype=dtype)

    def from_tuple(self, tpl: tuple, dtype=None):
        """
        Convert  a tuple into a numpy array object
        @param: self: object
        @param: tpl: a tuple
        return: a numpy array object
        """
        if type(tpl) != tuple:
            return None
        return asarray(tpl, dtype=dtype)

    def from_iterable(self, itr: Iterator, dtype=None):
        """
        Convert  a Iterator into a numpy array object
        @param: self: object
        @param: itr: a Iterator object
        return: a numpy array object
        """
        if type(itr) not in {Iterator, range, GeneratorExit}:
            return None
        return fromiter(itr, dtype=None)

    def from_shape(self, shape: tuple, value: float = 0, dtype=None):
        """
        Create a numpy array from a given shape with all element equal to value
        @param: shape: the given tuple as shape
        @param: value: a float number to fill the numpy array
        return: numpy array
        """
        if type(shape) != tuple:
            return None
        return full_like(float, value, shape=shape, dtype=dtype)

    def random(self, shape: tuple):
        """
        Create a numpy array from a given shape with random values
        @param: shape: a tuple with the shape
        return: numpy array
        """
        return rand(shape[0], shape[1])

    def identity(self, n: int, dtype=None):
        """
        Create a identity matrix
        @param: n: the matrix size
        return: a numpy array
        """
        return identity(n, dtype=dtype)
