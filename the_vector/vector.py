class Vector:
    """
    A class representing a vector with one column or one row
    """

    def __init__(self, values):
        self.values = values
        n_rows = len(values)
        self.shape = (1, len(*values)) if n_rows == 1 else (n_rows, 1)

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

    def __truediv__(self, other):
        """
        Implement division of one vector by a scalar number;
        @param: self: dividend of operation;
        @param: other: divisor of operation;
        return: a new vector with value as result of division.
        """
        return self * (1 / other)

    def __rtruediv(self, other):
        raise(ArithmeticError)

    def dot(self, other):
        """
        Calculate the dot product of two vectors
        @param: self: a vector object;
        @param: other: a vector object;
        return: a float.
        """
        pass

    def T(self):
        """
        Calculate the transpose vector.
        @param: self: the vector;
        return: a new vector who is the transpose of self
        """
        pass
