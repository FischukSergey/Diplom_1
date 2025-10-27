from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    """
    Тесты для класса Burger.
    """

    def test_init(self):
        """
        Тест инициализации бургера.
        """
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        """
        Тест установки булочки.
        """
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
