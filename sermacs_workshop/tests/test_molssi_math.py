"""
Tests for list_util module
"""
import sermacs_workshop as sermacs
import pytest


@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize("num_list, expected_mean", [([1, 2, 3, 4, 5], 3),
                                                     ([0, 2, 4, 6], 3),
                                                     ([1, 2, 3, 4], 2.5)])
def test_many(num_list, expected_mean):
    assert sermacs.mean(num_list) == expected_mean


def test_list_type():
    test_input = 47
    with pytest.raises(TypeError):
        sermacs.mean(test_input)


def test_list_length():
    test_input = []
    with pytest.raises(IndexError):
        sermacs.mean(test_input)


def test_mixed_type():
    test_input = [1, 2, 3.0, 4.0]
    test_mean = sermacs.mean(test_input)
    assert test_mean == 2.5


def test_item_types():
    test_input = [1, 2.0, 'a', "String"]
    with pytest.raises(TypeError):
        sermacs.mean(test_input)


def test_mean(num_list_3):
    assert sermacs.mean(num_list_3) == 3.0


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
