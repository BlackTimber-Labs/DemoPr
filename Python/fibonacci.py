def fibonacci_gen(max_number):
    """
    A generator function for creating the Fibonacci sequence up to a maximum number
    """
    a, b = 0, 1
    while a <= max_number:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    max_value = int(input("Generate Fibonacci up to which number? "))
    for number in fibonacci_gen(max_value):
        print(number)