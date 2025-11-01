import pytest
from praktikum.burger import Burger


@pytest.fixture
def burger():
    """
    Фикстура для создания экземпляра бургера.
    """
    return Burger()
