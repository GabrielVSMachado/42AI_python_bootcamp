from functools import reduce, singledispatchmethod


class Vector(object):
    """
    A class representing a vector with one column or one row
    """
    @singledispatchmethod
    def __init__(self, values):
        """
        Constructor when values is a array
        @param: *args: arguments passed to __init__ function
        return: call __init__ with arguments unchanged
        """
        self.values = values
        n_rows = len(values)
        self.shape = (1, len(*values)) if n_rows == 1 else (n_rows, 1)

    @__init__.register(tuple)
    def _(self, values: tuple):
        """
        Constructor when values is a tuple
        @param: *args: arguments passed to __init__
        return: None
        """
        if values[1][0] > values[1][1]:
            raise(ValueError(
                "The second value of range must be greater than the first")
            )
        self.values = [[i] for i in range(*values)]
        self.shape = (len(self.values), 1)

    @__init__.register(int)
    def _(self, values: int):
        """
        Constructor when values is a integer number
        @param: *args: arguments passed to __init__
        return: None
        """
        self.values = [[i] for i in range(values)]
        self.shape = (len(self.values), 1)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.values)

    def __mul__(self, other) -> object:
        """Implement multiplication between a vector object and a scalar number
        @param: self: the vector object
        @param: other: the scalar number
        return: A new vector with values as products
        """
        if type(other) != int and type(other) != float:
            raise("Only support product between a vector and a scalar")
        elif self.shape[0] == 1:
            return self.__class__([[num * other for num in self.values[0]]])
        else:
            return self.__class__(
                [*map(lambda x: [x[0] * other], self.values)])

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        """
        Implement addition of two vector with same shape.
        @param: self: the vector object;
        @param: other: the other vector object;
        return: A new vector with values as result of sum
        """
        if type(other) != Vector:
            raise("Only support sum of two object of type Vector")
        if self.shape != other.shape:
            raise("Only add vectors with same shape")
        if self.shape[0] == 1:
            return self.__class__(
                [[i + j for i, j in zip(*self.values, *other.values)]])
        return self.__class__(
            [*map(lambda x: [x[0][0] + x[1][0]],
                  zip(self.values, other.values))])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """
        Implement subtraction of two vectors with same shape.
        @param: self: minuend part of subtraction;
        @param: other: subtrahend part of subtraction;
        return: A new vector object with values as result of subtraction
        """
        return self + (other * -1)

    def __rsub__(self, other):
        return other + (self * -1)

    def __truediv__(self, other):
        """
        Implement division of one vector by a scalar number;
        @param: self: dividend of operation;
        @param: other: divisor of operation;
        return: a new vector with value as result of division.
        """
        return self * (1 / other)

    def __rtruediv__(self, other):
        raise(NotImplementedError)

    def dot(self, other):
        """
        Calculate the dot product of two vectors with same shape
        @param: self: a vector object;
        @param: other: a vector object;
        return: a float.
        """
        if self.shape != other.shape:
            raise(NotImplementedError(
                "Only implemented dot product of vectors with same shape"))
        if self.shape[0] == 1:
            return reduce(
                lambda x, y: x + y[0] * y[1],
                zip(*self.values, *other.values), 0)
        return reduce(
            lambda x, y: x + y[0][0] * y[1][0],
            zip(self.values, other.values), 0)

    def T(self):
        """
        Calculate the transpose vector.
        @param: self: the vector;
        return: a new vector whom is the transpose of self
        """
        if self.shape[0] == 1:
            return self.__class__([*map(lambda x: [x], *self.values)])
        return self.__class__([reduce(lambda x, y: x + y, self.values)])
