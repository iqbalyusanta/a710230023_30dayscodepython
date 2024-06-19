def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    else:
        return a/b

try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(e)
else:
    print("The result is:", result)