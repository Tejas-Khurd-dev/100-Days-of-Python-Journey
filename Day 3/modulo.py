num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

remain = num1 % num2
print(remain)
print("\n")
# ***---------------------------------------------------------------------***

check_num = int(input("Enter a number to whether it is even or odd: "))
if check_num % 2 == 0:
    print("Entered number is Even")
else:
    print("Entered number is odd")
