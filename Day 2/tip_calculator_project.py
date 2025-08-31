print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? $: "))
tip = int(input("What percentage tip would you like to give? 10 12 15:  "))
people = int(input("How many people to split the bill?: "))

total_bill = (tip / 100 * bill) + bill
each_person_bill = total_bill / people
print(f"Each person should pay: ${round(each_person_bill, 2)}\nThankyou")
