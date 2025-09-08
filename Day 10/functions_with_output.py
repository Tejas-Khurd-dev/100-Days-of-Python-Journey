# first_name: str → means first_name is expected to be a string.
# last_name: str → means last_name is expected to be a string.
# -> str → means the function will return a string.
def format_name(first_name: str, last_name: str) -> str:
    # Used .strip() to remove extra spaces
    return f"{first_name.strip().title()} {last_name.strip().title()}"


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Formatted Name:", format_name(first_name, last_name))
print("\n")
# ****************************************************************************

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("HeLlo"))
print(output)
