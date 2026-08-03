from recipe_cost_calculator import calculate_ingredient_cost


def test_flour_cost():
    cost = calculate_ingredient_cost(20, 1000, 250)
    assert cost == 5


def test_tomato_cost():
    cost = calculate_ingredient_cost(30, 500, 200)
    assert cost == 12


def test_one_full_package():
    cost = calculate_ingredient_cost(25, 1000, 1000)
    assert cost == 25
