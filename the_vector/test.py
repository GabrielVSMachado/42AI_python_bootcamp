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


def test_dot_product_of_two_line_vectors():
    result = Vector([[1., 3.]]).dot(Vector([[2., 4.]]))
    expected = 14
    assert result == expected


def test_dot_product_of_two_line_vectors_with_3_dimension():
    result = Vector([[1., 3., 5.]]).dot(Vector([[2., 4., 6.]]))
    expected = 44
    assert result == expected


def test_dot_product_of_two_column_vectors():
    result = Vector([[1], [2], [3]]).dot(Vector([[1], [2], [3]]))
    expected = 14
    assert result == expected


def test_dot_product_of_vectors_with_differents_shapes():
    try:
        Vector([[1], [2], [3]]).dot(Vector([[1, 2, 3]]))
        assert False
    except NotImplementedError:
        assert True


def test_division_of_one_vector_by_0():
    try:
        Vector([[1, 2, 3]]) / 0.
        assert False
    except ZeroDivisionError:
        assert True


def test_rdivision_expected_not_implemented_error():
    try:
        2 / Vector([[1, 2, 4]])
        assert False
    except NotImplementedError:
        assert True


def test_transposte_of_line_vector():
    result = Vector([[1, 2, 3]]).T()
    expected = Vector([[1], [2], [3]])
    assert result.values == expected.values


def test_transposte_of_column_vector():
    result = Vector([[1], [2], [3]]).T()
    expected = Vector([[1, 2, 3]])
    assert result.values == expected.values
