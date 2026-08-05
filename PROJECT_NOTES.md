# Project Notes

## Ingredient cost calculation 

The ingredient cost is calculated from the package price, package quantity and quantity used:

```text
cost per unit = package price / package quantity
ingredient cost = cost per unit * quantity used

Example:
Package quantity: 1,000 g
Package price: 20 DKK
Quantity used: 250 g

20 / 1000 * 250 = 5 DKK

## Data structure

Each ingredient is represented by a dictionary:
ingredient = {
    "name": "Flour",
    "quantity_used": 250,
    "unit": "g",
    "cost": 5,
}

The ingredient dictionaries are stored in a list:
ingredients = []
ingredients.append(ingredient)

## Main functions

calculate_ingredient_cost() calculates the cost of the quantity used
calculate_total_cost() adds the ingredient costs
calculate_cost_per_portion() divides the total cost by the number of portions
find_most_expensive_ingredient() finds the ingredient with the highest cost
get_text() prevents empty text input
get_positive_number() validates prices and quantities
get_positive_whole_number() validates whole-number input
main() controls the program flow

## Program flow

1. Ask for the recipe name
2. Ask for the number of portions and ingredients
3. Collect and validate the ingredient information
4. Store each ingredient in the list
5. Calculate the total cost and cost per portion
6. Identify the most expensive ingredient
7. Display the recipe summary

## Input validation

The input functions repeat their questions until valid values are entered. Number validation prevents invalid text from stopping the program and accepts both commas and full stops in decimal values.

## Tests

The pytest tests compare calculation results with expected values.

Run them with:
python -m pytest
