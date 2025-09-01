print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age <= 12:
        ticket_price = 5
        print("Your ticket price is $5.")
    elif age <= 18:
        ticket_price = 7
        print("Your ticket price is $7.")
    else:
        ticket_price = 12
        print("Your ticket price is $12.")

    wants_photo = input("Do you want photo token? Type y for Yes or n for No: ")

    if wants_photo == "y":
        ticket_price += 3

    print(f"\nYour total ticket price is ${ticket_price}")
else:
    print("Sorry you have to grow taller before you can ride.")
    