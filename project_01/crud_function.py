
from datetime import datetime
from function_file import save_expense_file, save_income_file, load_expense_file, load_income_file

# File path
file_name_income = "project_01/data/income.csv"
file_name_expense = "project_01/data/expense.csv"

# for Income

def create_income():
    income_list = load_income_file(file_name_income)
    
    if not income_list:
        iid = 1
        
    else:
        iid = max(int(income["iid"]) for income in income_list) + 1
        # hight_id_found = 0
        # for income in income_list:
        #     current_id = int(income["iid"])
        #     if current_id > hight_id_found:
        #         hight_id_found = current_id
        
        # iid = hight_id_found + 1
    
    iname = input("Enter the Income name: ")
    # date = input("Enter the Income Date(YY-MM-DD): ")
    # idate = datetime.strptime(date,"%y-%m-%d")
    
    date_input = input("Enter the Income Date(YY-MM-DD): ")
    
    # 1. Convert the user's string into a date object
    user_date = datetime.strptime(date_input, "%y-%m-%d").date()
    
    # 2. Get the current time from your computer right now
    current_time = datetime.now().time()
    
    # 3. Combine them together!
    idate = datetime.combine(user_date, current_time)
    
    
    idescription = input("Enter the Income description: ")
    iamount = float(input("Enter the Income amount: "))
    
    income_list.append({"iid": iid,"iname": iname, "idate": idate, "idescription": idescription, "iamount": iamount})
    save_income_file(file_name_income, income_list)
    print("Income added successfully!")

def view_income():
    income_list = load_income_file(file_name_income)
    
    print("\n" + "="*90)
    print(f"{'ID':<5} | {'Name':<12} | {'Date':<25} | {'Description':>20} | {'Amount':>10}")
    print("-" * 90)
        
    for income in income_list:
        print(f"{income["iid"]:<5} | {income['iname']:<12} | {income['idate']:<25} | {income['idescription']:>20} | ${income['iamount']:>10.2f}")
        
    print("="*90 + "\n")


def update_income():
    pass


def delete_income():
    pass


# for Expense

def create_expense():
    pass


def view_expense():
    pass


def update_expense():
    pass


def delete_expense():
    pass