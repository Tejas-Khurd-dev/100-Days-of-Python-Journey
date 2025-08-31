age = 12
print("My age:",age)
# print("My age:",age) → adds an extra space after the colon, because print inserts a space between arguments.
print("\n")
# ***---------------------------------------------------------------------***

print(5 + 5)
print(5 - 5)
print(2 * 5)
print(6 / 2) # --> This will give you answer in float type
print(6 // 2) # --> This will give you answer in int type
print(3 % 2) # --> Give Remainder
print(4 ** 2) # --> Meaning 4 raise to 2
print(3 + 3.0)  # --> Floating number operating with another int will always give floating number

print("\n")
# ***---------------------------------------------------------------------***


# PEMDAS
# 1. Parentheses ()
# 2. Exponent **
# 3. Multiplication / Division (* or /)
# 4. Addition / Subtracting (+ or -)

print(3 * 3 + 3 / 3 - 3)
# 3 * 3 + 3 / 3 - 3 --> 9 + 1.0 -3 --> 10.0 - 3 --> 7.0

print(3 * (3 + 3) / 3 - 3)
# 3 * (3 + 3) / 3 - 3 --> 3 * 6 / 3 - 3 --> 18 / 3 - 3 --> 6.0 - 3 --> 3.0

print("\n")
# ***---------------------------------------------------------------------***

height = 1.65  # in meters
weight = 84    # in kilograms

# Calculate BMI
bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi}")
# Here f string is used in above example
