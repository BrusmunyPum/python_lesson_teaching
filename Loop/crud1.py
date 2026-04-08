# CRUD = Create, Update, Read , Delete

products = []

while True:
    print("===========MENU============")
    print("1.Add product\n2.View\n3.Update\n4.Delete\n5.exit")
    option = int(input("Enter option: "))
    
    match option:
        case 1:
            name = input("Input product name: ")
            products.append(name)
            print(f"The product {name} is add successfully..")
            
        case 2:
            print("========== Product ==========")
            for product in products:
                print(product)
        
        case 3:
            product_name_update = input("Enter the product name that you want to update: ")
            
            if product_name_update in products:
                new_name = input("Enter new product name: ")
                # Find the index number of the item first
                index_number = products.index(product_name_update)
                # Update the list using that index number
                products[index_number] = new_name
                print("Product updated successfully!")
            else:
                print("Product not found")
                
        case 4:
            product_name_delete = input("Enter the product name that you want to update: ")
            if product_name_delete in products:
                products.remove(product_name_delete)
                print("Product delete successfully!")
                
        case 5:
            print("Exit.....")
            break
        
        case _:
            print("Please inter number betweeen 1 to 5")