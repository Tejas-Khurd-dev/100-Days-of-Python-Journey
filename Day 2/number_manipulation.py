height = 1.65  # in meters
weight = 84    # in kilograms

# Calculate BMI
bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi}") # Full floating-point value
print(f"Your BMI is: {int(bmi)}") # Floors (cuts off decimals)
print(f"Your BMI is: {round(bmi)}") # Rounds to nearest integer
print(f"Your BMI is: {round(bmi, 4)}")
# Python’s round(bmi, 4) does not guarantee fixed decimals when printing.
# It only computes the rounded value. When you print, Python might drop trailing digits

# To force exactly 4 digits after the decimal, use formatting:
print(f"Your BMI is: {bmi:.4f}")

print("\n")
# ***---------------------------------------------------------------------***

a = int("5") / int(2.7)
print(a)
# Prints answer in floating point number
print("\n")
# ***---------------------------------------------------------------------***

score = 0
score += 1
print(f"Your score is {score}")

# f-strings → gives you full control over formatting (no extra space unless you type it).
# f-strings can also handle formatting directly, e.g:

# pi = 3.14159
# print(f"Pi to 2 decimals: {pi:.2f}")  # Pi to 2 decimals: 3.14
