while True: 
    number = input("Enter a phone number: ")   
    if number.isdigit() and len(number) == 10:
        print("Number is valid. Congrats!")
        break
    else:
        print("Number is invalid. Try again. ")
        continue
    
    
