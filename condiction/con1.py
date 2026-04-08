
# user input
a = float(input("Enter value a : "))
b = float(input("Enter value b : "))
c = float(input("Enter value c : "))

# logic
delta = b**2 - 4*a*c


print(f"{a**2}x^2 + {b}x + {c} = 0")
print(f"delta = {delta}")
# check condiction
if delta > 0:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print(f"x1 = {x1} and x2 = {x2}")

elif delta == 0:
    x1 = x2 = -b/(2*a)
    print(f"x1 = x2 = {x1}")
    
else :
    print("This eqaution has root in complex values.!")