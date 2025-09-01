print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: # 45 <= age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#  Python have two more operators or, not

print("\n")
# ***---------------------------------------------------------------------***

print(not False == True)
print("\n")
# ***---------------------------------------------------------------------***

a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")

# choice 'B' is correct because the condition not a >= b evaluates to true
# (since 5 is not greater than or equal to 7), and the second part a != b is also true
# (because 5 is not equal to 7). Therefore, the code prints "B".
