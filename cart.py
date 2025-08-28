#Shopping Cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you would like to buy (e to exit): ")
    if food.lower() == "e":
        break
    else:
        price =float(input(f"Enter the amount of {food}: $ "))
        foods.append(food)
        prices.append(price)

print("----- SHOPING CART -----")

for food in foods:
    print(food, end= " ")

for price in prices:
    total+= price

print(f"\nYour total is $ {total}")
