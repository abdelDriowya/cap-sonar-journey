import pytest

from inventory.stock import Stock


def test_add_and_total():
    stock = Stock()
    stock.add("apple", 3)
    stock.add("apple", 2)
    assert stock.total() == 5


def test_remove_too_much():
    stock = Stock()
    stock.add("pear", 1)
    with pytest.raises(ValueError):
        stock.remove("pear", 2)
