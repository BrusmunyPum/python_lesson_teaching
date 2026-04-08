def total_amount(qty, price):
    return qty*price

def discount_amount(qty,price,discount_percent):
    return total_amount(qty,price) * (discount_percent/100)

def payment(qty,price,discount_percent):
    grand_total = total_amount(qty,price) - discount_amount(qty,price,discount_percent)
    return grand_total
        
def menu():
    print("================== MENU ==================")
    print("1.Add product\n2.View\n3.Update\n4.Delete\n5.Search\n6.Exit")
    print("==========================================")