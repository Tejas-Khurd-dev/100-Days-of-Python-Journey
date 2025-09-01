print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster.", end = " ")
    # In Python, the end parameter in the print() function controls what is printed at the end of the output.
    #  (end = " ") Add a space instead of newline:
    # by default end="\n", meaning a newline is added after each print
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Your ticket price is $5")
    elif age <= 18:
        print("Your ticket price is $7")
    else:
        print("Your ticket price is $12")
else:
    print("Sorry you have to grow taller before you can ride.")
    