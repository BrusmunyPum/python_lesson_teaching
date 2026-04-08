# MENU
print("============ CALCULATETOR ===============")
print("1. Add ( + ) \n2. Sub ( - ) \n3. Mul ( * ) \n4. Div ( / )\n5. Exit")
print("==========================================")

# using match statement

while True:
    # let one variable for comparision in math
    options = int(input("Enter your option : "))
    match options:
        case 1:
            a = float(input("Enter value a : "))
            b = float(input("Enter value b : "))
            print(f"a + b = {a+b}")
            
        case 2:
            a = float(input("Enter value a : "))
            b = float(input("Enter value b : "))
            print(f"a - b = {a-b}")
                
        case 3:
            a = float(input("Enter value a : "))
            b = float(input("Enter value b : "))
            print(f"a * b = {a*b}")
                 
        case 4:
            a = float(input("Enter value a : "))
            b = float(input("Enter value b : "))
            print(f"a / b = {a/b}")
        
        case 5:
            print("Programe is exit .......")    
            break
        
        case _:
            print("Invalid option!! please enter number between 1 to 4")
            