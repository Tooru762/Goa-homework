name = input("თქვენი სახელი: ")
print(greed(name))  # მილოცვა

# 2. შექმენით ბუტერბროტი
bread = input("დაასახელეთ პური: ")
filling = input("რა შევსება გსურთ? ")
toppings_input = input("დაასახელეთ დამატებითი ინგრედიენტები (გაერთოთ კომამით): ")
toppings = toppings_input.split(",") if toppings_input else []
