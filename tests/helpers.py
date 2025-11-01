"""
Вспомогательные функции для тестов.
"""

from unittest.mock import Mock


def create_mock_bun(price, name="test bun"):
    """
    Создаёт мок булочки с заданной ценой и названием.

    :param price: Цена булочки
    :param name: Название булочки
    :return: Mock объект булочки
    """
    mock_bun = Mock()
    mock_bun.get_price.return_value = price
    mock_bun.get_name.return_value = name
    return mock_bun


def create_mock_ingredient(price, name="test ingredient", ingredient_type="FILLING"):
    """
    Создаёт мок ингредиента с заданными параметрами.

    :param price: Цена ингредиента
    :param name: Название ингредиента
    :param ingredient_type: Тип ингредиента (FILLING или SAUCE)
    :return: Mock объект ингредиента
    """
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_type.return_value = ingredient_type
    return mock_ingredient


def add_ingredients_to_burger(burger, ingredients):
    """
    Добавляет список ингредиентов в бургер.

    :param burger: Экземпляр бургера
    :param ingredients: Список ингредиентов для добавления
    """
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)


def create_mock_ingredients_list(count, with_names=False):
    """
    Создаёт список мок-объектов ингредиентов.

    :param count: Количество моков для создания
    :param with_names: Если True, каждый мок получит уникальное имя
    :return: Список Mock объектов
    """
    mock_ingredients = []
    for i in range(count):
        if with_names:
            mock_ingredients.append(Mock(name=f"ingredient_{i}"))
        else:
            mock_ingredients.append(Mock())
    return mock_ingredients
