from function_file import load_file, save_file
from static_data import file_name
from utils import total_amount, payment

def check_go_or_back():
    # Asks user to proceed or return to menu.
    choose = input("Do you want to process? (y/n): ").lower()
    if choose == "n" or choose == "no":
        return False
    
    return True

def inputData():
    # Call the function correctly with ()
    if not check_go_or_back():
        print("Operation cancelled. Returning to menu...")
        return
    
    # Load existing products
    pt = load_file(file_name)   
    
    # Take data input from user (Fixed nested quotes)
    code = f"P{input('Enter the code : ')}"
    name = input("Enter the name: ")
    qty = int(input("Enter the quantity: "))
    price = float(input("Enter the unit price($): "))
    discount = float(input("Enter the discount(%): "))
    
    # Calculate totals
    total = total_amount(qty, price)
    final_payment = payment(qty, price, discount)

    # Update and save
    pt.append({
        "code": code, 
        "name": name, 
        "qty": qty, 
        "price": price, 
        "discount": discount
    })
    
    save_file(file_name, pt)
    print("Product added successfully!")
    return code, name, qty, price, discount, total, final_payment

def view_product():
    if not check_go_or_back():
        return
    
    pt = load_file(file_name)
    
    print("\n" + "="*70)
    print(f"{'Code':<6} | {'Name':<25} | {'Qty':>5} | {'Price':>10} | {'Disc%':>8}")
    print("-" * 70)
        
    for p in pt:
        # Using .get() is safer in case a key is missing
        print(f"{p['code']:<6} | {p['name']:<25} | {p['qty']:>5} | ${p['price']:>9.2f} | {p['discount']:>7}%")
    print("="*70 + "\n")

def update_product():
    if not check_go_or_back():
        return

    pt = load_file(file_name)
    update_code = f"P{input('Enter the code to update: ')}"
    update_status = False
    
    for p in pt:
        if p["code"] == update_code:
            p["name"] = input("Enter the new name: ")
            p["qty"] = int(input("Enter the new quantity: "))
            p["price"] = float(input("Enter the new unit price($): "))
            p["discount"] = float(input("Enter the new discount(%): "))
            update_status = True
            break # Stop searching once found
    
    if update_status:
        save_file(file_name, pt)
        print("Update successfully!")
    else:
        print("Product not found!")

def delete_product():
    if not check_go_or_back():
        return

    pt = load_file(file_name)
    delete_code = f"P{input('Enter the code to delete: ')}"
    
    # Use list comprehension for cleaner deletion
    new_pt = [p for p in pt if p["code"] != delete_code]
    
    if len(new_pt) < len(pt):
        save_file(file_name, new_pt)
        print("Delete successfully!")
    else:
        print("Product not found!")