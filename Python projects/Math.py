import math

radius = float(input("Enter the redius of a circle: "))

circumfarence = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"The circumfarence of the circle is {round(circumfarence, 3)}cm ")
print(f"\nThe area of the circle is {round(area, 2)}cm")