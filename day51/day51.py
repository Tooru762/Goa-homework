my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_list = [1, 2, 3]
my_list.append(4)  # Adding an element
my_list.remove(2)  # Removing an element
print("Updated List:", my_list)
my_list = [3, 1, 4, 2, 5]
my_list.sort()
print("Sorted List:", my_list)
squares = [x**2 for x in range(1, 6)]
print("List Comprehension Result:", squares)
my_list = [10, 20, 30]
print("Length of List:", len(my_list))
num = 10
if num > 5:
    print("Number is greater than 5")
num = 4
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
num = 0
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
num = 15
if num > 10:
    if num % 3 == 0:
        print("Number is greater than 10 and divisible by 3")
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print("Number is", result)
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
count = 1
while count <= 5:
    if count == 3:
        break
    print("Count:", count)
    count += 1
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count:", count)
while True:
    print("This is an infinite loop")
    break  # Stopping the infinite loop
my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print("Element:", my_list[index])
    index += 1
for i in range(1, 6):
    print("Number:", i)
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:
    print("Fruit:", fruit)
for i in range(5):
    print("Index:", i)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
for num in range(1, 6):
    print("Number:", num)
else:
    print("Loop completed successfully")
