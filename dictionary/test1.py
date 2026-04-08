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
    {"pid": 110, "pname": "Notebook", "pqty": 200, "pcat": "Stationery", "price": 4.99},
    {"pid": 111, "pname": "Mechanical Keyboard", "pqty": 30, "pcat": "Electronics", "price": 75.00},
    {"pid": 112, "pname": "Mechanical Keyboard", "pqty": 30, "pcat": "Electronics", "price": 75.00}
]

# for item in products:
#     print(item["pid"])

# name_input = input("Input name: ").lower()
# print(name_input)
# print(products[1]["pname"].lower())

# print(name_input in products[1]["pname"].lower())

# if name_input in products[1]["pname"].lower():
#     print(f"{products[1]['pid']:<5} | {products[1]['pname']:<30} | {products[1]['pcat']:<30} | {products[1]['pqty']:>5} | ${products[1]['price']:>9.2f}")


# print(f"{products[0]["pid"]}, {products[0]["pname"]}, {products[0]["pcat"]}, {products[0]["price"]}")


display_list = []

# dsplay all data in list

# display_list = products

# 2. display by pid
# id_search = int(input("Input ID: "))

name_input = input("Input name: ").lower()

# print(id_search == products[1]["pid"])

# for x in products:
#     # print(id_search == x["pid"])
#     if id_search == x["pid"]:
#         display_list.append(x)

for x in products:
    print(name_input in x["pname"].lower())
    if name_input in x["pname"].lower():
        display_list.append(x)


print(display_list)