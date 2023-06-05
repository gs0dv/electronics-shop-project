"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.errors import InstantiateCSVError
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def item_f():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def item_p():
    return Phone("Смартфон", 10000, 20, 2)


def test_calculate_total_price(item_f):
    assert item_f.calculate_total_price() == 200000


def test_apply_discount(item_f):
    Item.pay_rate = 0.8
    item_f.apply_discount()
    assert item_f.price == 8000


def test_name(item_f):
    assert item_f.name == "Смартфон"


def test_name_2(item_f):
    with pytest.raises(Exception):
        item_f.name = "Смартфон_многобукав"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(item_f):
    assert repr(item_f) == "Item('Смартфон', 10000, 20)"


def test_str(item_f):
    assert str(item_f) == "Смартфон"


def test_add(item_f, item_p):
    assert (item_f + item_p) == 40
    assert (item_p + item_f) == 40


def test_add__ValueError(item_f):
    with pytest.raises(ValueError):
        item_f + 5


def test_instantiate_from_csv__FileNotFoundError():
    Item.path = ""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv__InstantiateCSVError():
    Item.path = 'test_items.csv'
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
