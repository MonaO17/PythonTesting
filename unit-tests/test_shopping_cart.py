from shopping_cart import ShoppingCart
import pytest
import ItemDatabase
from unittest.mock import Mock

# Nutze fixture um Redundanzen in test-Setups zu verringern. 
# Dazu muss die Fixture anschließend der Test-Funktion übergeben werden. 
# Eine Test-Funktion kann auch mehrere Fixtures engegennehmen
@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    # init
    cart.add("apple")
    
    # run & assert
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    # init
    cart.add("apple")
    
    # run & assert
    assert "apple" in cart.get_items()

def test_when_add_more_then_max_items_should_fail(cart):
    # init
    for _ in range(5):
         cart.add("apple")
    
    # run & assert
    with pytest.raises(OverflowError):
        cart.add("apple")

def test_can_get_total_price(cart):
    # init
    cart.add("apple")
    cart.add("orange")
    price_map = {
        "apple": 1.0,
        "orange": 2.0
    }

    # run & assert
    assert cart.get_total_price(price_map) == 3.0

def test_can_get_total_price(cart):
    # init
    cart.add("apple")
    cart.add("orange")
    price_map = {
        "apple": 1.0,
        "orange": 2.0
    }

    # run & assert
    assert cart.get_total_price(price_map) == 3.0

# Bsp. Mock
def test_can_get_total_price(cart):
    # init
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    #item_database.get = Mock(return_value = 3.0)

    # run & assert
    assert cart.get_total_price(item_database) == 3.0



            