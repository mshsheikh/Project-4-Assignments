print("\n-- -- -- -- -- -- -- --")
print("   04 - DICTIONARIES     ")
print("      Pop Up Shop        ")
print("-- -- -- -- -- -- -- --\n")

fruit_prices = {
    "apples": 10.0,
    "bananas": 25.0,
    "mangos": 30.0,
    "oranges": 12.5,
    "guava": 7.0,
    "strawberries": 5.0
}

total_cost = 0.0

for fruit, price in fruit_prices.items():
    quantity = input(f'''Shopkeeper: How many ({fruit}) do you want?
Customer: ''')

    total_cost += int(quantity or 0) * price

print(f"\nYour total is ${total_cost}")

footer_A = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
