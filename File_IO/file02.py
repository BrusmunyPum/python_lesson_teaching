import csv
import os

products = [
    {"pid": 101, "pname": "Laptop", "pqty": 15, "pcat": "Electronics", "price": 899.99},
    {"pid": 102, "pname": "Wireless Mouse", "pqty": 50, "pcat": "Electronics", "price": 25.50},
    {"pid": 103, "pname": "Mechanical Keyboard", "pqty": 30, "pcat": "Electronics", "price": 75.00},
    {"pid": 104, "pname": "Coffee Maker", "pqty": 12, "pcat": "Home Goods", "price": 45.99},
    {"pid": 105, "pname": "Desk Lamp", "pqty": 40, "pcat": "Home Goods", "price": 18.25},
    {"pid": 106, "pname": "Office Chair", "pqty": 8, "pcat": "Furniture", "price": 120.00},
    {"pid": 107, "pname": "Water Bottle", "pqty": 100, "pcat": "Accessories", "price": 12.50},
    {"pid": 108, "pname": "Backpack", "pqty": 25, "pcat": "Accessories", "price": 55.00},
    {"pid": 109, "pname": "Smartphone", "pqty": 20, "pcat": "Electronics", "price": 699.00},
    {"pid": 110, "pname": "Notebook", "pqty": 200, "pcat": "Stationery", "price": 4.99}
]

file_path = "File_IO/products.csv"

file_exist = os.path.isfile(file_path)

# with open("File_IO/products.csv", "w", newline="") as file:
#     colum_header = ["pid","pname","pqty","pcat", "price"]
    
#     writer = csv.DictWriter(file, fieldnames=colum_header)
    
#     writer.writeheader()
    
#     for item in products:
#         writer.writerow(item)
        
# print("Success: Product save to csv file..\n")



with open(file_path, "a", newline="") as file:
    colum_header = ["pid", "pname", "pqty", "pcat", "price"]
    
    writer = csv.DictWriter(file, fieldnames=colum_header)
    
    # Only write the header if the file is new/doesn't exist yet
    if not file_exist:
        writer.writeheader()
    
    writer.writerow({"pid": 111, "pname": "Notebook", "pqty": 200, "pcat": "Stationery", "price": 4.99})
        
print("Success: Product appended and saved to csv file.\n")

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(f"ID: {row["pid"]}, NAME: {row["pname"]}, QTY: {row["pqty"]}, CATEGORY: {row["pcat"]}, PRICE: {row["price"]}")