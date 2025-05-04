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
