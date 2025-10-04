#exception handling 

try:
    num = int(input("Enter a number: "))
    print( 1 / num)
except ZeroDivisionError:
    print("You can't devide by zero.")

except ValueError:
    print("Enter numbers only.")
except Exception:
    print("Something went wrong.")

finally:
    print("Do some cleanup here ! ")