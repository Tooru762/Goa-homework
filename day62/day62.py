def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))  # Output: 3
 
 class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!

import csv

def average_scores(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            scores = list(map(int, row['Scores'].split(',')))
            avg = sum(scores) / len(scores)
            print(f"{name}: {avg:.2f}")

# Sample CSV:
# Name,Scores
# Alice,"90,85,88"
# Bob,"70,75,80"

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

add(5, 3)

