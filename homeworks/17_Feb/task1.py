from random import random


import random

a = random.randint(0, 9,)

# prompt
print(a)

b = input("Enter a number from 0 to 9: ")

if b.isdigit():
    b = int(b)
    if a == b:
        print("Yes!")
    else:
        print("No!")
else:
    print("Not a number")