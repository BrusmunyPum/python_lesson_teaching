# width = int(input("Enter Width : "))
# height = int(input("Enter Height : "))

# area = width * height

# p = (width + height)*2

# print(f"Width : {width} cm")
# print(f"Height : {height} cm")
# print(f"Area : {area} cm^2")
# print(f"Perimeter : {p} cm")


code = int(input("Enter code : "))
price = int(input("Enter price : "))
qty = int(input("Enter qty : "))
discount = int(input("Enter discount : "))

total = price * qty

# dicount_price = total * (discount / 100)

payment = total - (total * (discount / 100))

print(f"Code : {code} , Price : {price} , Qty : {qty} , Discount : {discount}")
print(f"Discount Price : {total * (discount / 100)}")
print(f"Total : {total}")
print(f"Payment : {payment}")

