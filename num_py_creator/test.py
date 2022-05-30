from NumPyCreator import NumPyCreator
from numpy import asarray, testing, fromiter, identity


def test_from_list_normal_input():
    x = NumPyCreator()
    result = x.from_list([[1,2,3],[4,5,6]])
    expected = asarray([[1,2,3],[4,5,6]])
    try:
        testing.assert_array_equal(result, expected)
        assert True
    except AssertionError:
        assert False


def test_from_list_with_wrong_dimensions():
    x = NumPyCreator()
    result = x.from_list([[1,2,3], [1,2]])
    assert result is None


def test_from_list_with_arg_as_tuple():
    x = NumPyCreator()
    result = x.from_list(((1, 2, 3), (1,2,3)))
    assert result is None


def test_from_tuple_normal_input():
    x = NumPyCreator()
    result = x.from_tuple(((1,2,3),(4,5,6)))
    expected = asarray(((1,2,3),(4,5,6)))
    try:
        testing.assert_array_equal(result, expected)
        assert True
    except AssertionError:
        assert False


def test_from_tuple_with_arg_as_list():
    x = NumPyCreator()
    result = x.from_tuple(['a', 'b', 'c'])
    assert result is None


def test_from_iterable_with_normal_input():
    x = NumPyCreator()
    result = x.from_iterable(range(5))
    expected = fromiter(range(5), dtype=None)
    try:
        testing.assert_array_equal(result, expected)
        assert True
    except AssertionError:
        assert False


def test_from_iterable_with_input_as_list():
    x = NumPyCreator()
    result = x.from_iterable([1, 2, 3])
    assert result is None


def test_from_shape_with_normal_input():
    x = NumPyCreator()
    result = x.from_shape((3,5))
    expected = asarray([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    try:
        testing.assert_array_equal(result, expected)
        assert True
    except AssertionError:
        assert False


def test_identity():
    x = NumPyCreator()
    result = x.identity(5, dtype='<U21')
    expected = identity(5, dtype='<U21')
    try:
        testing.assert_array_equal(result, expected)
        assert True
    except AssertionError:
        assert False
