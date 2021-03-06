"""Tests for https://www.codewars.com/kata/calculate-fibonacci-return-count-of-digit-occurrences."""

import pytest


TEST_FIB = [
    (1, 1),
    (3, 2),
    (20, 6765),
    (50, 12586269025),
    (99, 218922995834555169026),
]

TEST_DIGITS = [
(10, [(2, 5)]),
(10000, [
    (254, 3),(228, 2),(217, 6),(217, 0),(202, 5),(199, 1),(198, 7),(197, 8),
    (194, 4),(184, 9)
    ]),
(100000, [
    (2149, 2), (2135, 1), (2131, 8), (2118, 9), (2109, 0), (2096, 3), (2053, 5), (2051, 6), (2034, 7), (2023, 4)
    ]),
]


@pytest.mark.parametrize('n, result', TEST_FIB)
def test_generate_fib(n, result):
    """Test generate_fib returns correct Fibonacci numbers."""
    from fib_digit_occurence import generate_fib
    assert generate_fib(n) == result



@pytest.mark.parametrize('n, result', TEST_DIGITS)
def test_fib_digits(n, result):
    """Test fib_digits returns correct integer pairs."""
    from fib_digit_occurence import fib_digits
    assert fib_digits(n) == result
