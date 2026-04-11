import csv
from pathlib import Path

def save_file(file_name, product_list):
    # This line automatically creates ALL missing folders
    Path(file_name).parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_name, "w", newline="") as file:
        column_header = ["code", "name", "qty", "price", "discount"]
        writer = csv.DictWriter(file, fieldnames=column_header)
        writer.writeheader()
        writer.writerows(product_list)
    
    print("Save into file successfully....")
        
def load_file(file_name):
    product_list = []
    try: 
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["qty"] = int(row["qty"])
                row["price"] = float(row["price"])
                row["discount"] = float(row["discount"])
                
                product_list.append(row)
                
        return product_list
    
    except FileNotFoundError:
        print("we can not find this file....")
        return product_list