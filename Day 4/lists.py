fruits = ["Apple", "Orange", "Grapes", "Pear"]

train_name = "Tejas"
random = [24,"Bus-Stop", 3.145, train_name, True, ["Hello", "Hi"]]

print(fruits)
print(fruits[2])

print(random)
print(random[-2])

random[4] = False
print(random[4])

random.append(["Watermelon","Papaya"])
print(random)

fruits.extend(["Papaya", "Coconut"])
print(fruits)

