def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
def sum_of_differences(arr):
    return sum(arr[i] - arr[i + 1] for i in range(len(arr) - 1))
def digitize(n):
    return list(map(int, str(n)[::-1]))
def string_to_array(s):
    return s.split() if s else [""]
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
def solution(string):
    return string[::-1]
def remove_char(s):
    return s[1:-1]
11. Square(n) Sum
python
Copy code
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
 Find the smallest integer in the array
python
Copy code
def find_smallest_int(arr):
    return min(arr)
13. Filtering even numbers
python
Copy code
def filter_even_numbers(arr):
    return [x for x in arr if x % 2 == 0]
14. Summation
python
Copy code
def summation(num):
    return sum(range(1, num + 1))
15. Function 1 - Hello World
python
Copy code
def greet():
    return "Hello, World!"
16. Count of positives / sum of negatives
python
Copy code
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]
17. Remove String Spaces
python
Copy code
def no_space(x):
    return x.replace(" ", "")
18. You can't code under pressure #1
python
Copy code
def double_integer(i):
    return i * 2
19. Returning Strings
python
Copy code
def greet(name):
    return f"Hello, {name} how are you doing today?"
20. Convert a number to a string
python
Copy code
def number_to_string(num):
    return str(num)
21. Multiply
python
Copy code
def multiply(a, b):
    return a * b
22. Keep up the hoop
python
Copy code
def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"
23. Century From Year
python
Copy code
def century(year):
    return (year + 99) // 100
24. Beginner - Lost Without a Map
python
Copy code
def maps(a):
    return [x * 2 for x in a]
25. Sum Arrays
python
Copy code
def sum_array(a):
    return sum(a)
