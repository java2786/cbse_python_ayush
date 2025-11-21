def divide(x, y):
    assert y != 0, "Division by zero is not allowed"
    return x / y

# result = divide(10, 2)  # This will work
# print(result)  # Output: 5.0

result = divide(10, 0)  # This will raise an AssertionError
