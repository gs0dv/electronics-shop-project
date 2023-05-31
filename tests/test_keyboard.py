"""Тестирование модуля keyboard с помощью pytest"""
import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def kb_1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(kb_1):
    assert str(kb_1) == "Dark Project KD87A"


def test_str_lang(kb_1):
    assert str(kb_1.language) == "EN"
    kb_1.change_lang()
    assert str(kb_1.language) == "RU"
    kb_1.change_lang()
    kb_1.change_lang()
    assert str(kb_1.language) == "RU"


def test_set_lang__AttributeError(kb_1):
    with pytest.raises(AttributeError):
        kb_1.language = 'CH'
