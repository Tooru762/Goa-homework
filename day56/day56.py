# A simple calculator that adds two numbers
def add(a, b):
    return a + b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = add(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")
# This calculates the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
# Print the Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = int(input("Enter number of terms in Fibonacci sequence: "))
print(f"The Fibonacci sequence up to {terms} terms is: {fibonacci(terms)}")
# Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
