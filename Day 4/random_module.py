import random
import my_module

random_integer = random.randint(1,10)
# a <= int <= 10
print(random_integer)

print(my_module.pi_value)

random_number_between_0_to_1 = random.random() # Recommended use this as 0 is fix and you can extend other limit
# 0.0 <= number < 1.0
print(random_number_between_0_to_1)

random_number_between_0_to_1 = random.random() * 10
# 0.0 <= number < 10.0
print(random_number_between_0_to_1)

random_float = random.uniform(1,10)
# a <= int <= 10
print(random_float)

random_heads_or_tails = random.randint(0,1)

if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

