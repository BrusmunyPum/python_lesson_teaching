from utils import menu 
from function_crud import inputData, view_product
   
def task_option():
    while True:
        menu()
        option = int(input("Enter option ( 1-6 ): "))
        match option:
            case 1:
                inputData()
            case 2:
                view_product()
            case 6:
                print("Exit.....")
                break
            case _:
                print("Ivalid option please input the number between ( 1-6 )...!!")
                continue
    
