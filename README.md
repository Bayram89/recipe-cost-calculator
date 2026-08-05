# Recipe Cost Calculator

A Python command-line tool for calculating ingredient usage costs, total recipe cost and cost per portion.

The project is based on a common foodservice calculation: a recipe normally uses only part of an ingredient package, so its cost must be calculated from the package quantity, package price and quantity used.

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
- Show the most expensive ingredient
- Prevent empty recipe names, ingredient names, and units
- Accept only whole numbers for portions and ingredient counts
- Handle invalid number input without crashing
- Accept both commas and full stops in decimal numbers

## Technical overview

- Python command-line interface
- Functions for ingredient and recipe-cost calculations
- Lists and dictionaries for organising recipe data
- Input validation and error handling
- Support for comma and full-stop decimal input
- pytest tests for the main calculations

## Run the program

Python 3 is required. No external package is needed to run the calculator.

```bash
python recipe_cost_calculator.py
```

## Run the tests

Install pytest if needed:

```bash
python -m pip install pytest
```

Run:

```bash
python -m pytest
```

The project includes six tests covering ingredient cost, total cost, cost per portion and identification of the most expensive ingredient.

## Calculation notes

See [PROJECT_NOTES.md](PROJECT_NOTES.md) for details about the calculations, data structure, program flow, validation and tests.

## Limitations

- Recipes are kept only for the active program session
- Recipes are not saved after the program closes
- Ingredient quantities must use the same unit as their package quantity
