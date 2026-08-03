def calculate_ingredient_cost(package_price, package_quantity, quantity_used):
    cost_per_unit = package_price / package_quantity
    ingredient_cost = cost_per_unit * quantity_used
    return ingredient_cost


def get_text(question):
    while True:
        answer = input(question).strip()

        if answer != "":
            return answer

        print("Please enter a value.")


def get_positive_number(question):
    while True:
        try:
            number = float(input(question).replace(",", "."))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def get_positive_whole_number(question):
    while True:
        try:
            number = int(input(question))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("Recipe Cost Calculator")
    print("----------------------")

    recipe_name = get_text("Recipe name: ")
    portions = get_positive_whole_number("Number of portions: ")
    number_of_ingredients = get_positive_whole_number(
        "How many ingredients are in the recipe? "
    )

    ingredients = []
    total_cost = 0

    for number in range(number_of_ingredients):
        print(f"\nIngredient {number + 1}")

        ingredient_name = get_text("Ingredient name: ")
        unit = get_text("Unit (for example g, ml or piece): ")
        package_quantity = get_positive_number(
            f"Quantity in the package ({unit}): "
        )
        package_price = get_positive_number("Package price in DKK: ")
        quantity_used = get_positive_number(
            f"Quantity used in the recipe ({unit}): "
        )

        ingredient_cost = calculate_ingredient_cost(
            package_price,
            package_quantity,
            quantity_used,
        )

        ingredient = {
            "name": ingredient_name,
            "quantity_used": quantity_used,
            "unit": unit,
            "cost": ingredient_cost,
        }

        ingredients.append(ingredient)
        total_cost = total_cost + ingredient_cost

    cost_per_portion = total_cost / portions

    print("\nRecipe Summary")
    print("--------------")
    print(f"Recipe: {recipe_name}")
    print(f"Portions: {portions:g}")
    print("\nIngredients:")

    for ingredient in ingredients:
        print(
            f"- {ingredient['name']}: "
            f"{ingredient['quantity_used']:g} {ingredient['unit']} "
            f"= {ingredient['cost']:.2f} DKK"
        )

    print(f"\nTotal recipe cost: {total_cost:.2f} DKK")
    print(f"Cost per portion: {cost_per_portion:.2f} DKK")


if __name__ == "__main__":
    main()
