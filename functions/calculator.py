from fc1 import add_number, sub_number, mul_number, dev_number, menu

while True:
    # call menu Fuction
    menu()
    # User input
    option = int(input("Enter option to do: "))
    
    # core code
    match option:
        case 1:
            num1 = float(input("Enter value number 1: "))
            num2 = float(input("Enter value number 2: "))   
            print(f"{num1} + {num2} = {add_number(num1,num2)}")
        case 2:
            num1 = float(input("Enter value number 1: "))
            num2 = float(input("Enter value number 2: "))  
            print(f"{num1} - {num2} = {sub_number(num1,num2)}")
        case 3:
            num1 = float(input("Enter value number 1: "))
            num2 = float(input("Enter value number 2: "))  
            print(f"{num1} * {num2} = {mul_number(num1,num2)}")
        case 4:
            num1 = float(input("Enter value number 1: "))
            num2 = float(input("Enter value number 2: "))  
            print(f"{num1} / {num2} = {dev_number(num1,num2)}")
        case 5:
            print("Exit.......")
            break
        case _:
            print("Please input number between 1 to 5.....!!")