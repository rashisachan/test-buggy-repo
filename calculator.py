# calculator.py — intentionally buggy
def add(a, b):
    return a - b  # BUG: should be a + b

def multiply(a, b
    return a + b  # BUG: should be a * b

print(add(3, 2))       # prints 1, should be 5
print(multiply(3, 4))  # prints 7, should be 12
