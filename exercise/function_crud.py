from function_file import load_file, save_file
from static_data import file_name
from utils import total_amount, payment

def inputData():
    # call fuction load_file ( read file ), pt = product_list return from fuction
    pt = load_file(file_name)
    
    # take data input from user
    code = f"P{input("Enter the code : ")}"
    name = input("Enter the name: ")
    qty = int(input("Enter the quantity: "))
    price = float(input("Enter the unit price($): "))
    discount = float(input("Enter the discount(%): "))
    
    # update the product list data
    pt.append({"code": code, "name": name, "qty": qty, "price": price, "discount": discount})
    # total
    total = total_amount(qty,price)
    #payment
    final_payment = payment(qty,price,discount)
    
    # save to file
    save_file(file_name,pt)
    return code,name,qty,price,discount,total,final_payment


def view_product():
    # call fuction load_file ( read file ), pt = product_list return from fuction
    pt = load_file(file_name)
    
    print("\n-----------------------> List Product <--------------------------")
    print(f"{'Code':<5} | {'Name':<30} | {'Qty':>5}pcs | ${'Price':>10} | %{'discount':>10}")
    print("-" * 65)
        
    for product in pt:
        print(f"{product['code']:<5} | {product['name']:<30} | {product['qty']:>5} | ${product['price']:>9.2f} | ${product['discount']:>9.2f}")
        
    print("\n")
    
def update_product():
    pt = load_file(file_name)
    update_code = f"P{input("Enter the code : ")}"
    
    update_status = False
    
    for p in pt:
        if update_code in p["code"]:
            p["name"] = input("Enter the new name: ")
            p["qty"] = int(input("Enter the new quantity: "))
            p["price"] = float(input("Enter the new unit price($): "))
            p["discount"] = int(input("Enter the new discount(%): "))
            update_status = True
    
    if update_status :
        print("Update successfully..")
    else:
        print("Product not found!!..")

    save_file(file_name,pt)

def delete_product():
    pt = load_file(file_name)
    delete_code = f"P{input("Enter the code : ")}"
    
    delete_status = False
    
    for p in pt:
        if delete_code in p["code"]:
            pt.remove(p)
            delete_status = True
    
    if delete_status :
        print("Delete successfully..")
    else:
        print("Product not found!!..")

    save_file(file_name,pt)