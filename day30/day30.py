def check_even_or_odd():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number % 2 == 0:
        print(f"{number} არის ლუწი.")
    else:
        print(f"{number} არის კენტი.")

def check_positive_or_negative():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number > 0:
        print(f"{number} არის დადებითი.")
    elif number < 0:
        print(f"{number} არის უარყოფითი.")
    else:
        print("რიცხვი არის ნულოვანი.")

def check_multiple_of_five():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number % 5 == 0:
        print(f"{number} არის ხუთის ჯერადი.")
    else:
        print(f"{number} არ არის ხუთის ჯერადი.")

def check_age():
    age = int(input("შეიყვანეთ ასაკი: "))
    if age >= 18:
        print("თქვენ ხართ სრულწლოვანი.")
    else:
        print("თქვენ ხართ არასრულწლოვანი.")

def check_square():
    side_length = float(input("შეიყვანეთ კვადრატის მხარის სიგრძე: "))
    area = side_length ** 2
    print(f"კვადრატის ფართობია: {area}")

def check_password():
    while True:
        password = input("შეიყვანეთ პაროლი: ")
        if len(password) >= 8:
            print("რეგისტრაციამ წარმატებით ჩაიარა.")
            break
        else:
            print("პაროლი უნდა შეიცავდეს 8 სიმბოლოს ან მეტს, გთხოვთ ხელახლა შეიყვანოთ.")

def squares_of_numbers():
    numbers = []
    for _ in range(10):
        number = int(input("შეიყვანეთ რიცხვი: "))
        numbers.append(number)
    
    print("რიცხვების კვადრატები:")
    for number in numbers:
        print(f"{number} -> {number ** 2}")

# ფუნქციების გაწვდვა
check_even_or_odd()
check_positive_or_negative()
check_multiple_of_five()
check_age()
check_square()
check_password()
squares_of_numbers()
