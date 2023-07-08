import pytest

from example_package_yeerahdi.example_square import square_number


@pytest.mark.parametrize("test_input,expected", [(2, 4), (-1, 1), (0, 0)])
def test_square_number(test_input, expected):
    assert square_number(test_input) == expected