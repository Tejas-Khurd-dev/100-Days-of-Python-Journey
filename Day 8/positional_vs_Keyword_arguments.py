# Functions with input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Are you in {location}?")


greet_with("Jack Bauer", "Mumbai")


def sum_of_two_numbers(num1, num2):
    print(num1 + num2)

#Key word arguments
sum_of_two_numbers(num2 = 2,num1 = 2)
