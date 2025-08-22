#Begginer friendly claculator in python

Operator = input("Enter an operator (+, -, *, /): ")
Num1 = int(input("Enter the 1st number: "))
Num2 = int(input("Enter the 2nd number: "))

if Operator == "+":
    result = Num1 + Num2
    print(f"The sum is {result}")
elif Operator == "-":
    result = Num1 - Num2
    print(result)
elif Operator == "*":
    result = Num1 * Num2
    print(round(result, 2))
elif Operator == "/":
    result = Num1 / Num2
    print(round(result, 2))
else:
    print(f"{Operator} is not a valid operator")