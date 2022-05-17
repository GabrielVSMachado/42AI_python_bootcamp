from vector import Vector


def test_multiplication_between_vector_c_and_scalar_2():
    c = Vector([[1.], [2.], [3.]])
    result = c * 2
    expected = [[2.], [4.], [6.]]
    assert result.values == expected


def test_multiplication_between_vector_d_and_scalar_2():
    d = Vector([[1., 2., 3.]])
    result = d * 2
    expected = [[2., 4., 6.]]
    assert result.values == expected


def test_reversed_multiplication_vector_d_and_scalar_2():
    d = Vector([[1., 2., 3.]])
    result = 2 * d
    expected = [[2., 4., 6.]]
    assert result.values == expected


def test_add_two_columns_vector():
    result = Vector([[1.], [2.], [3.]]) + Vector([[1.], [2.], [3.]])
    expected = [[2.], [4.], [6.]]
    assert result.values == expected


def test_add_two_row_vectors():
    result = Vector([[1, 2, 3]]) + Vector([[1, 2, 3]])
    expected = [[2, 4, 6]]
    assert result.values == expected
