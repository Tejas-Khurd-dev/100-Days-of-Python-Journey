for i in range(6): # 0 to 5
    print(i, end = " ")

print()

for i in range(0, 11):
    print(i, end = " ")

print()

for i in range(0, 11, 2):
    print(i, end = " ")

print("\n")
# ***---------------------------------------------------------------------***

#  Adding number from 1 to 100

total_sum = 0
for number in range (0,101):
    total_sum += number
print(f"The sum of the numbers between 1 to 100 is: {total_sum}")
