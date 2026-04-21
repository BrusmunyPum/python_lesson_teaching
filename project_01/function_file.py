import csv
from pathlib import Path

def save_income_file(file_name, product_list):
    # This line automatically creates ALL missing folders
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_name, "w", newline="") as file:
        column_header = ["iid", "iname", "idate", "idescription","iamount"]
        writer = csv.DictWriter(file, fieldnames=column_header)
        writer.writeheader()
        writer.writerows(product_list)
    
    print("Save into file successfully....")
        
def load_income_file(file_name):
    product_list = []
    try: 
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["iid"] = int(row["iid"])
                row["iamount"] = float(row["iamount"])
                product_list.append(row)
                
        return product_list
    
    except FileNotFoundError:
        print("we can not find this file....")
        return product_list
    
    
def save_expense_file(file_name, product_list):
    # This line automatically creates ALL missing folders
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_name, "w", newline="") as file:
        column_header = ["eid", "ename", "edate", "edescription", "eamount"]
        writer = csv.DictWriter(file, fieldnames=column_header)
        writer.writeheader()
        writer.writerows(product_list)
    
    print("Save into file successfully....")
        
def load_expense_file(file_name):
    product_list = []
    try: 
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["eid"] = int(row["eid"])
                row["eamount"] = int(row["eamount"])              
                product_list.append(row)
                
        return product_list
    
    except FileNotFoundError:
        print("we can not find this file....")
        return product_list