"""Тесты с использованием pytest для класса phone.py"""
import pytest

from src.phone import Phone


@pytest.fixture()
def phone_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(phone_1):
    assert phone_1.number_of_sim == 2


def test_set_number_of_sim(phone_1):
    phone_1.number_of_sim = 4
    assert phone_1.number_of_sim == 4


def test_set_number_of_sim__ValueError(phone_1):
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 2.2
        phone_1.number_of_sim = 0


def test_str(phone_1):
    assert str(phone_1) == 'iPhone 14'


def test_repr(phone_1):
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"
