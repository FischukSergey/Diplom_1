from praktikum.bun import Bun
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
        burger.set_buns(Bun("black bun", 100))
        assert burger.bun.get_name() == "black bun"
        assert burger.bun.get_price() == 100