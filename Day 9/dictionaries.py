programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}

colours_of_fruits = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

#Will print "green"
print(colours_of_fruits["pear"], "\n")

#Adding item in dictionary
colours_of_fruits["peach"] = "pink"

#Edition item in dictionary
colours_of_fruits["pear"] = "light green"
print(colours_of_fruits, "\n")

my_empty_dictionary = {}

# Wiping a existing dictionary
programming_dictionary = my_empty_dictionary
#or programming_dictionary = {}
print(programming_dictionary, "\n")


# Loop through dictionary
for key in colours_of_fruits:
    print(key, end = " - ")
    print(colours_of_fruits[key])
