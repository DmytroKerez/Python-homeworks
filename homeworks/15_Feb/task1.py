my_str1 = input("Write a string: ")

if len(my_str1)>2:
    print(my_str1[0:2] + my_str1[-2:])
elif len(my_str1) == 2:
    print(my_str1*2)
else:
    print("Empty String")
