## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

## Результат тестирования

====================================================== test session starts 
platform darwin -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/sergeymac/dev/Python/Diplom/Diplom_1
plugins: allure-pytest-2.15.0, html-4.1.1, xdist-3.8.0, metadata-3.1.1, rerunfailures-16.1, cov-7.0.0
collected 25 items                                                                                                               

tests/test_burger.py ......................... [100%]

========================================================= tests coverage 
________________________________________ coverage: platform darwin, python 3.13.5-final-0 

Name                            Stmts   Miss  Cover   Missing
-------------------------------------------------------------
praktikum/__init__.py               0      0   100%
praktikum/bun.py                    8      4    50%   8-9, 12, 15
praktikum/burger.py                27      0   100%
praktikum/database.py              21     21     0%   1-33
praktikum/ingredient.py            11      6    45%   9-11, 14, 17, 20
praktikum/ingredient_types.py       2      2     0%   6-7
-------------------------------------------------------------
TOTAL                              69     33    52%
======================================================= 25 passed in 0.27s 
