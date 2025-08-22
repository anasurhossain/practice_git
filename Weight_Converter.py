#A simple weight converter program in python
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds ? (kg or lbs): ")

if unit == "kg":
    weight *= 2.205
    unit = "lbs"
    print(f"Your weight is {round(weight,2)} {unit}")
elif unit == "lbs":
    weight /= 2.205
    unit = "Kg"
    print(f"Your weight is {round(weight,1)} {unit}")
else:
    print(f"{weight} is not valid.")