import sum
import pytest_mock
import pytest

def test_somma() -> None:
    assert sum.sum(1, 2) == 3
    assert type(sum.sum(1, 2)) == int