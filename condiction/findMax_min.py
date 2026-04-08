# user input
n1 = float(input("Enter value n1 : "))
n2 = float(input("Enter value n2 : "))
n3 = float(input("Enter value n3 : "))
n4 = float(input("Enter value n4 : "))
n5 = float(input("Enter value n5 : "))

# logical 

total = n1 + n2 + n3 + n4 + n5
avg = total / 5

print(f"Total = {total}")
print(f"Average = {avg}")

# initialize valiue of maxNum and minNum
maxNum = n1
minNum = n1

# condiction

# for max
if maxNum < n2:
    maxNum = n2
    
if maxNum < n3:
    maxNum = n3
    
if maxNum < n4:
    maxNum = n4

if maxNum < n5:
    maxNum = n5
    
# for min

if minNum > n2:
    minNum = n2
    
if minNum > n3:
    minNum = n3
    
if minNum > n4:
    minNum = n4

if minNum > n5:
    minNum = n5


print(f"Max = {maxNum}")
print(f"Min = {minNum}")

print(f"Max: {max(n1, n2, n3, n4, n5)}")
print(f"Min: {min(n1, n2, n3, n4, n5)}")