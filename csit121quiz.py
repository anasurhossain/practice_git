class NotEvenError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"{self.value} is not an even number"

class EvenOnly:
    def __init__(self, value):
        self.value = value
        self.check_even()
    
    def check_even(self):
        if self.value % 2 == 0:
            print(self.value)
        else:
            raise NotEvenError(self.value)

# Test cases
try:
    e = EvenOnly(4)  # Should print 4
except NotEvenError as ne:
    print(ne)

try:
    e = EvenOnly(3)  # Should raise NotEvenError and print the error message
except NotEvenError as ne:
    print(ne)
