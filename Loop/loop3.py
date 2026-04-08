# main_number = 12
# count_loop = 5

import random

main_number = random.randint(1,20)

while True:
    guest_number = int(input("Enter number between 1-20 : "))
    
    if guest_number < main_number:
        print("The number is smaller!!\nplease input again")
    elif guest_number > main_number:
        print("The number is higher!!\nplease input again")
    else:
        print(f"The number {main_number} is correct. Congratulation.....")
        break
    
