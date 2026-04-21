# income = i_name, i_date, i_description, i_amount
# expense = e_name, e_date, e_description, e_amount

from crud_function import create_income, view_income
from utilts import main_menu, menu_expense, menu_income

def main():
    while True:
        main_menu()
        option = int(input("Enter your option: "))
        
        match option:
            case 1:
                while True:
                    menu_income()
                    income_option = int(input("Please input your income option here: "))
                    match income_option:
                        case 1:
                            create_income()
                        
                        case 2:
                            view_income()
                            
                        case 3:
                            # update
                            pass
                        
                        case 4:
                            # delete
                            pass
                        
                        case 5:
                            print("Exit income proccess......")
                            break
                        
                        case _:
                            print(" PLease inpute number between 1 to 5...!!")
            case 2:
                while True:
                    menu_expense()
                    expense_option = int(input("Please input your income option here: "))
                    match expense_option:
                        case 1:
                            # create
                            pass
                        case 2:
                            # vieew
                            pass
                        case 3:
                            # update
                            pass
                        case 4:
                            # delete
                            pass
                        
                        case 5:
                            print("Exit income proccess......")
                            break
                        
                        case _:
                            print(" PLease inpute number between 1 to 5...!!")
                
            case 3:
                print("Exit.......")
                break
                
            case _:
                print(" PLease inpute number between 1 to 3...!!")

if __name__ == "__main__":
    main()