"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture()
def item_f():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_f):
    assert item_f.calculate_total_price() == 200000


def test_apply_discount(item_f):
    Item.pay_rate = 0.8
    item_f.apply_discount()
    assert item_f.price == 8000