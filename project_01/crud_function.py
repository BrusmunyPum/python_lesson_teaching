
from datetime import datetime
from function_file import save_expense_file, save_income_file, load_expense_file, load_income_file

# File path
file_name_income = "project_01/data/income.csv"
file_name_expense = "project_01/data/expense.csv"


# for Income

def create_income():
    income_list = load_income_file(file_name_income)
    
    iname = input("Enter the Income name: ")
    date = input("Enter the Income Date(YY-MM-DD): ")
    idate = datetime.strptime(date,"%y-%m-%d")
    idescription = input("Enter the Income description: ")
    iamount = float(input("Enter the Income amount: "))
    
    income_list.append({"iname": iname, "idate": idate, "idescription": idescription, "iamount": iamount})
    save_income_file(file_name_income, income_list)
    print("Product added successfully!")

def view_income():
    pass


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