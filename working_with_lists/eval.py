from functools import reduce


class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        """
        Calculate the sum of lenght of which word in words weighted by a list
        of coefficients.
        @param: coefs: a list of floats;
        @param: words: a list of strings;
        return: a float.
        """
        if len(coefs) != len(words):
            return -1
        return reduce(
                lambda x, y: x + y[0] * len(y[1]),
                zip(coefs, words), 0
                )

    @staticmethod
    def enumerate_evaluate(coefs, words):
        """
        Calculate the sum of lenght of which word in words weighted by a list
        of coefficients.
        @param: coefs: a list of floats;
        @param: words: a list of strings;
        return: a float.
        """
        if len(coefs) != len(words):
            return -1
        result = 0.
        for key, value in enumerate(words):
            result += len(value) * coefs[key]
        return result
