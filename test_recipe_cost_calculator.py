from recipe_cost_calculator import calculate_cost_per_portion
from recipe_cost_calculator import calculate_ingredient_cost
from recipe_cost_calculator import calculate_total_cost
from recipe_cost_calculator import find_most_expensive_ingredient


def test_flour_cost():
    cost = calculate_ingredient_cost(20, 1000, 250)
    assert cost == 5


def test_tomato_cost():
    cost = calculate_ingredient_cost(30, 500, 200)
    assert cost == 12


def test_one_full_package():
    cost = calculate_ingredient_cost(25, 1000, 1000)
    assert cost == 25


def test_total_recipe_cost():
    ingredients = [
        {"name": "Tomatoes", "cost": 12},
        {"name": "Cream", "cost": 20},
    ]

    total_cost = calculate_total_cost(ingredients)
    assert total_cost == 32


def test_cost_per_portion():
    cost_per_portion = calculate_cost_per_portion(32, 10)
    assert cost_per_portion == 3.2


def test_most_expensive_ingredient():
    ingredients = [
        {"name": "Tomatoes", "cost": 12},
        {"name": "Cream", "cost": 20},
    ]

    most_expensive = find_most_expensive_ingredient(ingredients)
    assert most_expensive["name"] == "Cream"
