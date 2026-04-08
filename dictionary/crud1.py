# CRUD = Create, Update, Read , Delete
# product = pid, pname, price, pqty, pcategory = pcat

# products = {}
# products = []

products = [
    {"pid": 101, "pname": "Laptop", "pqty": 15, "pcat": "Electronics", "price": 899.99},
    {"pid": 102, "pname": "Wireless Mouse", "pqty": 50, "pcat": "Electronics", "price": 25.50},
    {"pid": 103, "pname": "Mechanical Keyboard", "pqty": 30, "pcat": "Electronics", "price": 75.00},
    {"pid": 104, "pname": "Coffee Maker", "pqty": 12, "pcat": "Home Goods", "price": 45.99},
    {"pid": 105, "pname": "Desk Lamp", "pqty": 40, "pcat": "Home Goods", "price": 18.25},
    {"pid": 106, "pname": "Office Chair", "pqty": 8, "pcat": "Furniture", "price": 120.00},
    {"pid": 107, "pname": "Water Bottle", "pqty": 100, "pcat": "Accessories", "price": 12.50},
    {"pid": 108, "pname": "Backpack", "pqty": 25, "pcat": "Accessories", "price": 55.00},
    {"pid": 109, "pname": "Smartphone", "pqty": 20, "pcat": "Electronics", "price": 699.00},
    {"pid": 110, "pname": "Notebook", "pqty": 200, "pcat": "Stationery", "price": 4.99}
]

while True:
    print("=========== MENU ============")
    print("1.Add product\n2.View\n3.Update\n4.Delete\n5.Search\n6.Exit")
    option = int(input("Enter option: "))
    
    match option:
        case 1:
            print("---------------------> Add Product <------------------")
            pid = int(input("Input product ID        : "))
            pname = input("Input product Name        : ")
            pqty = int(input("Input product Quantity : "))
            pcat = input("Input product Category     : ")
            price = float(input("Input product Price   : "))
            
            # products.update({"pid": pid,"pane": pname, "pqty": pqty, "pcat": pcat, "price": price})
            # Store the product using 'pid' as the unique key
            # products[pid] = {
            #     "pname": pname, 
            #     "pqty": pqty, 
            #     "pcat": pcat, 
            #     "price": price
            # }
            
            products.append({"pid": pid,"pname": pname, "pqty": pqty, "pcat": pcat, "price": price})
            print("Product add successfully!!....\n\n")
        
        # case 2:
        #     print("-----------------------> List Product <--------------------------")
      
        #     print(f"{'ID':<5} | {'Name':<30} | {'Category':<30} | {'Qty':>5} | {'Price':>10}")
        #     print("-" * 65)
   
        #     for details in products:
        #         print(f"{details['pid']:<5} | {details['pname']:<30} | {details['pcat']:<30} | {details['pqty']:>5} | ${details['price']:>9.2f}")
                
        #     print("\n\n")
        
        case 2:
           while True:
                print("============= View Menu ===============")
                print("1. View All Products\n2. Filter by Name\n3. Filter by Category\n4. Filter by Price\n5. Exit")
                view_op = int(input("Enter option: "))
                
                # Create an empty list to hold the products we want to show
                filtered_products = []
                
                match view_op:
                    case 1:
                        # If they want all, just copy the whole list
                        filtered_products = products 
                        
                    case 2:
                        filter_name = input("Enter the Name to filter by: ").lower()
                        for p in products:
                            if filter_name in p["pname"].lower():
                                filtered_products.append(p)
                                
                    case 3:
                        filter_cat = input("Enter the Category to filter by: ").lower()
                        for p in products:
                            if filter_cat in p["pcat"].lower():
                                filtered_products.append(p)
                                
                    case 4:
                        filter_price = float(input("Enter the exact Price to filter by: "))
                        for p in products:
                            if p["price"] == filter_price:
                                filtered_products.append(p)
                    
                    case 5:
                        print("Exit Viewing product .....!\n\n")
                        break
                    
                    case _:
                        print("Invalid option. Please enter a number between 1 and 4.")
                        # Skip the printing part if they entered a bad option
                        continue 

                # Now, we print whatever ended up in our filtered_products list!
                if not filtered_products:
                    print("\nNo products found matching that filter!!...")
                else:
                    print("\n-----------------------> List Product <--------------------------")
                    print(f"{'ID':<5} | {'Name':<30} | {'Category':<30} | {'Qty':>5} | {'Price':>10}")
                    print("-" * 65)
        
                    for product in filtered_products:
                        print(f"{product['pid']:<5} | {product['pname']:<30} | {product['pcat']:<30} | {product['pqty']:>5} | ${product['price']:>9.2f}")
                    print("\n")
            
        case 3:
            update_id = int(input("Input the product ID that you want to update: "))
            
            update_check = False
            
            for product in products:
                if product["pid"] == update_id:
                    # print(f"Updating product: {product['pname']}")
                    # # We ask for new details and overwrite the old ones in the dictionary
                    # product['pname'] = input("Input new Name     : ")
                    # product['pqty'] = int(input("Input new Quantity : "))
                    # product['pcat'] = input("Input new Category : ")
                    # product['price'] = float(input("Input new Price    : "))
                    # print("\nProduct updated successfully!!....")
                    
                    while True:
                        print("============= Update Menu ===============")
                        print("1.Update Name\n2.Update Quantity\n3.Update Category\n4.Update Price\n5.Update All\n6.Exit")
                        update_option = int(input("Enter option that you want to update: "))
                        match update_option:
                            case 1:
                                print(f"Updating product: {product['pname']}")
                                product['pname'] = input("Input new Name     : ")
                                print("\nProduct updated successfully!!....")
                            
                            case 2:
                                print(f"Updating product: {product['pname']}")
                                product['pqty'] = int(input("Input new Quantity : "))
                                print("\nProduct updated successfully!!....")
                            
                            case 3:
                                print(f"Updating product: {product['pname']}")
                                product['pcat'] = input("Input new Category : ")
                                print("\nProduct updated successfully!!....")
                                
                            case 4:
                                print(f"Updating product: {product['pname']}")
                                product['price'] = float(input("Input new Price    : "))
                                print("\nProduct updated successfully!!....")
                                
                            case 5:
                                print(f"Updating product: {product['pname']}")
                                product['pname'] = input("Input new Name     : ")
                                product['pqty'] = int(input("Input new Quantity : "))
                                product['pcat'] = input("Input new Category : ")
                                product['price'] = float(input("Input new Price    : "))
                                print("\nProduct updated successfully!!....")
                                
                            case 6:
                                print("Exit update.......")
                                break
                            
                            case _:
                                print("Please inter number betweeen 1 to 6 for update product")
                            
                        update_check = True
                       
            if not update_check :
                print("\nProduct is not found!!....")
            
        case 4:
            delete_id = int(input("Input the product ID that you want to Delete: "))
            delete_check = False
            
            for product in products:
                if product["pid"] == delete_id:
                    pro_delete_name = product["pname"]
                    products.remove(product)
                    print(f"\nProduct {pro_delete_name} was deleted successfully!!....")
                    delete_check = True
                    break
                    
            if not delete_check:
                print("The product is not found!!...")
        
        case 5:  
            while True:
                print("============= Search Menu ===============")
                print("1. Search by ID\n2. Search by Name\n3. Search by Category\n4. Search by Price\n5. Exit")
                search_op = int(input("Enter option that you want to search: "))
                search_check = False
                
                match search_op:
                    case 1:
                        search_id = int(input("Input the product ID that you want to Search: "))
                        print("\n-----------------------> Search Results <--------------------------")
                        print(f"{'ID':<5} | {'Name':<30} | {'Category':<30} | {'Qty':>5} | {'Price':>10}")
                        print("-" * 65)
                        
                        for product in products:
                            if product["pid"] == search_id:
                                print(f"{product['pid']:<5} | {product['pname']:<30} | {product['pcat']:<30} | {product['pqty']:>5} | ${product['price']:>9.2f}")
                                search_check = True
                                
                        if not search_check:
                            print("The product is not found!!...")
                            
                    case 2:
                        search_name = input("Input the product name that you want to Search: ").lower()
                        print("\n-----------------------> Search Results <--------------------------")
                        print(f"{'ID':<5} | {'Name':<30} | {'Category':<30} | {'Qty':>5} | {'Price':>10}")
                        print("-" * 65)
                        
                        for product in products:
                            if search_name in product["pname"].lower():
                                print(f"{product['pid']:<5} | {product['pname']:<30} | {product['pcat']:<30} | {product['pqty']:>5} | ${product['price']:>9.2f}")
                                search_check = True
                                
                        if not search_check:
                            print("The product is not found!!...")
                    
                    case 3:
                        search_cat = input("Input the product category that you want to Search: ").lower()
                        print("\n-----------------------> Search Results <--------------------------")
                        print(f"{'ID':<5} | {'Name':<30} | {'Category':<30} | {'Qty':>5} | {'Price':>10}")
                        print("-" * 65)
                        
                        for product in products:
                            if search_cat in product["pcat"].lower():
                                print(f"{product['pid']:<5} | {product['pname']:<30} | {product['pcat']:<30} | {product['pqty']:>5} | ${product['price']:>9.2f}")
                                search_check = True
                                
                        if not search_check:
                            print("The product is not found!!...")

                    case 4:
                        search_price = float(input("Input the product price that you want to Search: "))
                        print("\n-----------------------> Search Results <--------------------------")
                        print(f"{'ID':<5} | {'Name':<30} | {'Category':<30} | {'Qty':>5} | {'Price':>10}")
                        print("-" * 65)
                        
                        for product in products:
                            if product["price"] == search_price:
                                print(f"{product['pid']:<5} | {product['pname']:<30} | {product['pcat']:<30} | {product['pqty']:>5} | ${product['price']:>9.2f}")
                                search_check = True
                                
                        if not search_check:
                            print("The product is not found!!...")
                            
                    case 5:
                        print("Exit Search Product........\n\n")
                        break

                    case _:
                        print("Invalid option. Please enter a number between 1 and 5.")
        
        case 6:
            print("Exit.....")
            break
        
        case _:
            print("Please inter number betweeen 1 to 5")
            
            
            