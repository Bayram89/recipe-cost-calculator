# Learning Notes

These notes explain the main parts of the Recipe Cost Calculator in simple
language.

## The ingredient cost formula

The program first calculates the cost of one unit:

```text
cost per unit = package price / package quantity
```

It then calculates the cost of the quantity used:

```text
ingredient cost = cost per unit * quantity used
```

Example:

```text
A 1,000 g bag of flour costs 20 DKK.
The recipe uses 250 g.
20 / 1000 * 250 = 5 DKK
```

## How ingredients are stored

One ingredient is stored in a dictionary:

```python
ingredient = {
    "name": "Flour",
    "quantity_used": 250,
    "unit": "g",
    "cost": 5,
}
```

All ingredient dictionaries are stored in a list:

```python
ingredients = []
ingredients.append(ingredient)
```

## What the functions do

- `calculate_ingredient_cost()` calculates the cost of the amount used.
- `calculate_total_cost()` adds all ingredient costs together.
- `calculate_cost_per_portion()` divides the total cost by the portions.
- `find_most_expensive_ingredient()` finds the highest ingredient cost.
- `get_text()` prevents empty text input.
- `get_positive_number()` accepts positive prices and quantities.
- `get_positive_whole_number()` accepts whole-number counts.
- `main()` controls the order in which the program runs.

## How the program runs

1. Ask for the recipe name.
2. Ask for the number of portions and ingredients.
3. Use a loop to collect every ingredient.
4. Store each ingredient dictionary in a list.
5. Calculate the total and cost per portion.
6. Find the most expensive ingredient.
7. Print the recipe summary.

## Input validation

The program uses `while True` to repeat a question until the input is valid.

`try` and `except` prevent the program from crashing when text is entered where
a number is expected.

## Tests

The tests use small example values and `assert` to compare the actual result
with the expected result.

Run them with:

```bash
python -m pytest
```
