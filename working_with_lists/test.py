from eval import Evaluator


def test_zip_evaluate_with_5_words():
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    assert Evaluator.zip_evaluate(coefs, words) == 32.0


def test_enumerate_evaluate_with_7_words():
    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    assert Evaluator.enumerate_evaluate(coefs, words) == -1
