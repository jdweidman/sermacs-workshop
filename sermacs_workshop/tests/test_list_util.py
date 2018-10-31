"""
Tests for list_util module
"""
import sermacs_workshop as sermacs
import pytest


#@pytest.mark.skip
def test_title_case():
    test_string = "thIs IS a TesT sTrinG"
    title_string = sermacs.title_case(test_string)
    assert title_string == "This Is a Test String"


def test_type_failure():
    test_input = ['This', 'is', 'a', 'test']

    with pytest.raises(TypeError):
        sermacs.title_case(test_input)


#@pytest.mark.skip
def test_length():
    empty_string = ''

    with pytest.raises(IndexError):
        title_string = sermacs.title_case(empty_string)
