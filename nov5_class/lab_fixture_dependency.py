import pytest

# ---------- FIXTURES ---------- #

@pytest.fixture
def product_data():
    """Base fixture with product info"""
    return {"name": "Laptop", "price": 50000}


@pytest.fixture
def product_with_discount(product_data):
    """Fixture depending on another fixture"""
    product = product_data.copy()
    product["discount"] = 10  # 10% off
    product["final_price"] = product["price"] - (product["price"] * product["discount"] / 100)
    return product


@pytest.fixture
def complete_order(product_with_discount):
    """Fixture depending on multiple layers"""
    order = {
        "product": product_with_discount,
        "quantity": 2,
        "total_amount": product_with_discount["final_price"] * 2
    }
    return order


# ---------- TESTS ---------- #

def test_product_with_discount(product_with_discount):
    assert product_with_discount["name"] == "Laptop"
    assert product_with_discount["discount"] == 10
    assert product_with_discount["final_price"] == 45000


def test_complete_order(complete_order):
    assert complete_order["product"]["name"] == "Laptop"
    assert complete_order["quantity"] == 2
    assert complete_order["total_amount"] == 90000
