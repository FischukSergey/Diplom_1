from unittest.mock import Mock
import pytest
from tests.helpers import (
    create_mock_bun,
    create_mock_ingredient,
    create_mock_ingredients_list,
    add_ingredients_to_burger,
)


class TestBurger:
    """
    Тесты для класса Burger.
    """

    def test_init(self, burger):
        """
        Тест инициализации бургера.
        """
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger):
        """
        Тест установки булочки.
        """
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_single(self, burger):
        """
        Тест добавления одного ингредиента.
        """
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize("count", [1, 2, 3, 5])
    def test_add_ingredient_multiple(self, burger, count):
        """
        Тест добавления нескольких ингредиентов.
        """
        mock_ingredients = create_mock_ingredients_list(count)
        add_ingredients_to_burger(burger, mock_ingredients)

        assert len(burger.ingredients) == count
        assert burger.ingredients == mock_ingredients

    @pytest.mark.parametrize(
        "total_count,index_to_remove",
        [
            (3, 0),  # Удаление первого
            (3, 1),  # Удаление среднего
            (3, 2),  # Удаление последнего
            (1, 0),  # Удаление единственного
        ],
    )
    def test_remove_ingredient_by_index(self, burger, total_count, index_to_remove):
        """
        Тест удаления ингредиента по индексу.
        """
        mock_ingredients = create_mock_ingredients_list(total_count)
        add_ingredients_to_burger(burger, mock_ingredients)
        removed_ingredient = mock_ingredients[index_to_remove]

        burger.remove_ingredient(index_to_remove)

        assert len(burger.ingredients) == total_count - 1
        assert removed_ingredient not in burger.ingredients

    @pytest.mark.parametrize(
        "initial_positions,from_index,to_index,expected_order",
        [
            ([0, 1, 2], 0, 2, [1, 2, 0]),  # Перемещение первого в конец
            ([0, 1, 2], 2, 0, [2, 0, 1]),  # Перемещение последнего в начало
            ([0, 1, 2, 3], 1, 3, [0, 2, 3, 1]),  # Перемещение из середины в конец
            ([0, 1, 2, 3], 3, 1, [0, 3, 1, 2]),  # Перемещение из конца в середину
        ],
    )
    def test_move_ingredient_positions(
        self, burger, initial_positions, from_index, to_index, expected_order
    ):
        """
        Тест перемещения ингредиентов между позициями.
        """
        mock_ingredients = create_mock_ingredients_list(
            len(initial_positions), with_names=True
        )
        add_ingredients_to_burger(burger, mock_ingredients)

        burger.move_ingredient(from_index, to_index)

        expected_ingredients = [mock_ingredients[i] for i in expected_order]
        assert burger.ingredients == expected_ingredients

    def test_get_price_with_bun_only(self, burger):
        """
        Тест расчёта цены бургера только с булочкой (без ингредиентов).
        """
        mock_bun = create_mock_bun(price=50.0)
        burger.set_buns(mock_bun)

        price = burger.get_price()

        assert price == 100.0  # 50.0 * 2

    @pytest.mark.parametrize(
        "bun_price,ingredient_prices,expected_price",
        [
            (50.0, [10.0], 110.0),  # Булочка + 1 ингредиент
            (50.0, [10.0, 20.0], 130.0),  # Булочка + 2 ингредиента
            (100.0, [15.0, 25.0, 30.0], 270.0),  # Булочка + 3 ингредиента
            (75.0, [], 150.0),  # Только булочка
        ],
    )
    def test_get_price_with_ingredients(
        self, burger, bun_price, ingredient_prices, expected_price
    ):
        """
        Тест расчёта цены бургера с различными комбинациями ингредиентов.
        """
        mock_bun = create_mock_bun(price=bun_price)
        burger.set_buns(mock_bun)
        mock_ingredients = [
            create_mock_ingredient(price=price) for price in ingredient_prices
        ]
        add_ingredients_to_burger(burger, mock_ingredients)

        assert burger.get_price() == expected_price

    def test_get_receipt_format(self, burger):
        """
        Тест формата чека бургера.
        """
        mock_bun = create_mock_bun(price=100.0, name="black bun")
        burger.set_buns(mock_bun)
        mock_ingredient = create_mock_ingredient(
            price=50.0, name="sausage", ingredient_type="FILLING"
        )
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling sausage =\n"
            "(==== black bun ====)\n\n"
            "Price: 250.0"
        )
        assert receipt == expected_receipt

    @pytest.mark.parametrize(
        "bun_name,ingredients_data",
        [
            ("white bun", []),  # Без ингредиентов
            ("black bun", [("SAUCE", "hot sauce")]),  # С одним соусом
            (
                "red bun",
                [("FILLING", "cutlet"), ("SAUCE", "ketchup")],
            ),  # С начинкой и соусом
            (
                "sesame bun",
                [("FILLING", "cheese"), ("FILLING", "bacon"), ("SAUCE", "mayo")],
            ),  # Много ингредиентов
        ],
    )
    def test_get_receipt_with_ingredients(self, burger, bun_name, ingredients_data):
        """
        Тест чека с различными комбинациями ингредиентов.
        """
        mock_bun = create_mock_bun(price=100.0, name=bun_name)
        burger.set_buns(mock_bun)
        mock_ingredients = [
            create_mock_ingredient(price=50.0, name=name, ingredient_type=ing_type)
            for ing_type, name in ingredients_data
        ]
        add_ingredients_to_burger(burger, mock_ingredients)

        receipt = burger.get_receipt()

        assert receipt.count(bun_name) == 2
        for ingredient_type, ingredient_name in ingredients_data:
            assert ingredient_name in receipt
            assert ingredient_type.lower() in receipt
        assert "Price:" in receipt
