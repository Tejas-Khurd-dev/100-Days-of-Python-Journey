# len(12345) --> len function don't want to work with int
print("\n")
# ***---------------------------------------------------------------------***

print(type("string"))
print(type(123))
print(type(3.24))
print(type(True))

print(type(int))
# Why output is <class 'type'>?
# int itself is a class in Python (the class for integers).
# type(int) asks: what is the type of the class int?
# In Python, all classes are created by the metaclass type.
# So you get <class 'type'>.
print("\n")
# ***---------------------------------------------------------------------***

# Type Conversion
print(int("23"))
print(int("23") + int("7"))
print(int(2.5))
print(float(2))
print(str(123) + str(345))
print(bool("True"))
print(type(bool("True")))
print(str(True))
print(type(str(True)))

# ***---------------------------------------------------------------------***

# Quiz
print("Number of letters in your name: " + str(len(input("Enter your name: ")))
