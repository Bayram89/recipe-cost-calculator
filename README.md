# Recipe Cost Calculator

A beginner-friendly command-line program written in Python. It calculates how
much the ingredients used in a recipe cost, the total recipe cost, and the cost
per portion.

I built this project while learning Python fundamentals. The idea is connected
to a real foodservice problem: a recipe usually uses only part of an ingredient
package, so the cost of the amount used must be calculated.

## Example calculation

A 1,000 g bag of flour costs 20 DKK and a recipe uses 250 g:

```text
20 / 1000 * 250 = 5 DKK
```

The program repeats this calculation for every ingredient and adds the costs
together.

## Features

- Enter a recipe name and number of portions
- Add multiple ingredients
- Enter package quantity, package price, and quantity used
- Calculate the cost of each ingredient used
- Calculate the total recipe cost
- Calculate the cost per portion
- Handle invalid number input without crashing
- Accept both commas and full stops in decimal numbers

## Python concepts practised

- Variables and basic data types
- User input and printed output
- Mathematical calculations
- `if` statements
- `for` and `while` loops
- Lists and dictionaries
- Functions
- `try` and `except`

## Run the program

Python 3 is required. No external package is needed to run the calculator.

```bash
python recipe_cost_calculator.py
```

## Run the tests

The tests use pytest:

```bash
python -m pytest
```

## Limitations

This is intentionally a small beginner project. Recipes are not saved after the
program closes, and all ingredient quantities must use the same unit as their
package quantity.

## Possible future improvements

- Save recipes to a JSON file
- Edit or delete ingredients
- Add a simple Flask webpage
- Add a suggested selling price
