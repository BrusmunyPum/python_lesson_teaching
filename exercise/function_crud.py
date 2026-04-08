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
    price = float(input("Enter the the unit price($): "))
    discount = int(input("Enter the discount(%): "))
    
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