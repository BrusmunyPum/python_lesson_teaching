
# scores = float(input("Enter you score : "))

# if scores >= 90:
#     print("A")

# elif scores >= 80:
#     print("B")

# elif scores >= 70:
#     print("C")
    
# elif scores >= 60:
#     print("D")
    
# elif scores >= 50:
#     print("E")
    
# else:
#     print("F")

# 14

while True:
    ages = int(input("Enter your age : "))

    # if ages <= 12 :
    #     print("Ticket price 5$")
        
    # elif ages >= 65 | ages <= 89 :
    #     print("Ticket price 8$")
        
    # elif ages >= 90 :
    #     print("Ticket price Free")
        
    # else :
    #     print("Ticket price 12$")
    
    match ages:
        case ages if ages <= 12:
            print("Ticket price 5$")
        case ages if ages >= 65 | ages <= 89:
            print("Ticket price 8$")
        case ages if ages >= 90:
            print("Ticket price Free")
        case _:
            print("Ticket price 12$")
            
   
