# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")
try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("You have typed an invalid number, please try again with a numerical response such as 15.")
    age = int(input("How old are you?\n"))

if age >= 18:
    print(f"You can drive at age {age}.")
