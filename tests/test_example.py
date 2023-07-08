import pytest

from example_package_yeerahdi.example import add_one, square_number


def test_add_one():
    assert add_one(4) == 5


@pytest.mark.parametrize("test_input,expected", [(2, 4), (-1, 1), (0, 0)])
def test_square_number(test_input, expected):
    assert square_number(test_input) == expected
