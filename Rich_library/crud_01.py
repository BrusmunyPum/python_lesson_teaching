import csv
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Initialize the Rich Console
console = Console()

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

file_path = "File_IO/products_data.csv"
colum_header = ["pid", "pname", "pqty", "pcat", "price"]

# Ensure the directory exists so it doesn't crash on first run
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Helper function to draw beautiful tables anywhere in the code
def display_product_table(prod_list, title="Product List"):
    table = Table(title=f"[bold cyan]{title}[/bold cyan]", show_lines=True)
    
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Category", justify="center", style="blue")
    table.add_column("Qty", justify="center", style="yellow")
    table.add_column("Price", justify="right", style="bold green")

    for product in prod_list:
        table.add_row(
            str(product['pid']), 
            product['pname'], 
            product['pcat'], 
            str(product['pqty']), 
            f"${product['price']:.2f}"
        )
    console.print(table)


console.print(Panel("[bold green]Welcome to the Product Management System![/bold green]", expand=False))

try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["pid"] = int(row["pid"])
            row["pqty"] = int(row["pqty"])
            row["price"] = float(row["price"])
            
    console.print("[dim green]Data read and converted successfully...[/dim green]\n")
    
except FileNotFoundError:
    console.print("[yellow]We cannot find this file, creating a new one...[/yellow]")
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=colum_header)
        writer.writeheader()
        writer.writerows(products)


while True:
    menu_text = (
        "[bold cyan]1.[/bold cyan] Add Product\n"
        "[bold cyan]2.[/bold cyan] View\n"
        "[bold cyan]3.[/bold cyan] Update\n"
        "[bold cyan]4.[/bold cyan] Delete\n"
        "[bold cyan]5.[/bold cyan] Search\n"
        "[bold red]6.[/bold red] Exit"
    )
    console.print(Panel(menu_text, title="[bold yellow]=========== MENU ===========[/bold yellow]", expand=False))
    
    try:
        option = int(console.input("[bold white]Enter option: [/bold white]"))
    except ValueError:
        console.print("[bold red]Please enter a valid number![/bold red]\n")
        continue
    
    match option:
        case 1:
            load_data = []
            try:
                with open(file_path, "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        row["pid"] = int(row["pid"])
                        row["pqty"] = int(row["pqty"])
                        row["price"] = float(row["price"])
                        load_data.append(row)
            except FileNotFoundError:
                pass
            
            console.print("\n[bold yellow]---------------------> Add Product <------------------[/bold yellow]")
            pid = int(console.input("[cyan]Input product ID       : [/cyan]"))
            pname = console.input("[cyan]Input product Name     : [/cyan]")
            pqty = int(console.input("[cyan]Input product Quantity : [/cyan]"))
            pcat = console.input("[cyan]Input product Category : [/cyan]")
            price = float(console.input("[cyan]Input product Price    : [/cyan]"))
            
            load_data.append({"pid": pid,"pname": pname, "pqty": pqty, "pcat": pcat, "price": price})
            
            with open(file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=colum_header)
                writer.writeheader()
                writer.writerows(load_data)
            
            console.print("[bold green]✔ Product added successfully!![/bold green]\n")
        
        case 2:
           while True:
                view_menu = "1. View All\n2. Filter by Name\n3. Filter by Category\n4. Filter by Price\n5. Exit"
                console.print(Panel(view_menu, title="[bold blue]View Menu[/bold blue]", expand=False))
                view_op = int(console.input("[bold white]Enter option: [/bold white]"))
                
                view_files = []
                try:
                    with open(file_path, "r") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            row["pid"] = int(row["pid"])
                            row["pqty"] = int(row["pqty"])
                            row["price"] = float(row["price"])
                            view_files.append(row)
                except FileNotFoundError:
                    pass
                
                filtered_products = []
                
                match view_op:
                    case 1:
                        filtered_products = view_files
                    case 2:
                        filter_name = console.input("[cyan]Enter the Name to filter by: [/cyan]").lower()
                        filtered_products = [p for p in view_files if filter_name in p["pname"].lower()]
                    case 3:
                        filter_cat = console.input("[cyan]Enter the Category to filter by: [/cyan]").lower()
                        filtered_products = [p for p in view_files if filter_cat in p["pcat"].lower()]
                    case 4:
                        filter_price = float(console.input("[cyan]Enter the exact Price to filter by: [/cyan]"))
                        filtered_products = [p for p in view_files if p["price"] == filter_price]
                    case 5:
                        console.print("[bold red]Exiting View Menu...\[/bold red]\n")
                        break
                    case _:
                        console.print("[bold red]Invalid option![/bold red]")
                        continue 

                if not filtered_products:
                    console.print("[bold red]No products found matching that filter!![/bold red]\n")
                else:
                    display_product_table(filtered_products, title="Filtered Products")
            
        case 3:
            update_id = int(console.input("[bold cyan]Input the product ID you want to update: [/bold cyan]"))
            update_check = False
            update_products = []
            
            try:
                with open(file_path, "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        row["pid"] = int(row["pid"])
                        row["pqty"] = int(row["pqty"])
                        row["price"] = float(row["price"])
                        update_products.append(row)
            except FileNotFoundError:
                pass
            
            for product in update_products:
                if product["pid"] == update_id:
                    while True:
                        up_menu = "1. Name\n2. Quantity\n3. Category\n4. Price\n5. All\n6. Exit"
                        console.print(Panel(up_menu, title="[bold blue]Update Menu[/bold blue]", expand=False))
                        update_option = int(console.input("[bold white]Enter update option: [/bold white]"))
                        
                        match update_option:
                            case 1:
                                product['pname'] = console.input(f"[cyan]Input new Name for {product['pname']}: [/cyan]")
                            case 2:
                                product['pqty'] = int(console.input(f"[cyan]Input new Quantity for {product['pname']}: [/cyan]"))
                            case 3:
                                product['pcat'] = console.input(f"[cyan]Input new Category for {product['pname']}: [/cyan]")
                            case 4:
                                product['price'] = float(console.input(f"[cyan]Input new Price for {product['pname']}: [/cyan]"))
                            case 5:
                                product['pname'] = console.input("[cyan]Input new Name     : [/cyan]")
                                product['pqty'] = int(console.input("[cyan]Input new Quantity : [/cyan]"))
                                product['pcat'] = console.input("[cyan]Input new Category : [/cyan]")
                                product['price'] = float(console.input("[cyan]Input new Price    : [/cyan]"))
                            case 6:
                                break
                            case _:
                                console.print("[bold red]Invalid option![/bold red]")
                                continue
                                
                        console.print("[bold green]✔ Product updated successfully!![/bold green]\n")
                        update_check = True
                       
            if not update_check:
                console.print("[bold red]✖ Product is not found!![/bold red]\n")
                
            with open(file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=colum_header)
                writer.writeheader()
                writer.writerows(update_products)
            
        case 4:
            delete_id = int(console.input("[bold red]Input the product ID you want to Delete: [/bold red]"))
            delete_check = False
            delete_products = []
            
            try:
                with open(file_path, "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        row["pid"] = int(row["pid"])
                        row["pqty"] = int(row["pqty"])
                        row["price"] = float(row["price"])
                        delete_products.append(row)
            except FileNotFoundError:
                pass
            
            for product in delete_products:
                if product["pid"] == delete_id:
                    pro_delete_name = product["pname"]
                    delete_products.remove(product)
                    console.print(f"[bold green]✔ Product '{pro_delete_name}' was deleted successfully!![/bold green]\n")
                    delete_check = True
                    break
                    
            if not delete_check:
                console.print("[bold red]✖ Product is not found!![/bold red]\n")
                
            with open(file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=colum_header)
                writer.writeheader()
                writer.writerows(delete_products)
        
        case 5:  
            while True:
                search_menu = "1. By ID\n2. By Name\n3. By Category\n4. By Price\n5. Exit"
                console.print(Panel(search_menu, title="[bold magenta]Search Menu[/bold magenta]", expand=False))
                search_op = int(console.input("[bold white]Enter search option: [/bold white]"))
                
                search_files = []
                try:
                    with open(file_path, "r") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            row["pid"] = int(row["pid"])
                            row["pqty"] = int(row["pqty"])
                            row["price"] = float(row["price"])
                            search_files.append(row)
                except FileNotFoundError:
                    pass
                
                search_results = []

                match search_op:
                    case 1:
                        search_id = int(console.input("[cyan]Input ID to search: [/cyan]"))
                        search_results = [p for p in search_files if p["pid"] == search_id]
                    case 2:
                        search_name = console.input("[cyan]Input Name to search: [/cyan]").lower()
                        search_results = [p for p in search_files if search_name in p["pname"].lower()]
                    case 3:
                        search_cat = console.input("[cyan]Input Category to search: [/cyan]").lower()
                        search_results = [p for p in search_files if search_cat in p["pcat"].lower()]
                    case 4:
                        search_price = float(console.input("[cyan]Input Price to search: [/cyan]"))
                        search_results = [p for p in search_files if p["price"] == search_price]
                    case 5:
                        console.print("[bold red]Exiting Search...[/bold red]\n")
                        break
                    case _:
                        console.print("[bold red]Invalid option.[/bold red]")
                        continue
                
                if search_results:
                    display_product_table(search_results, title="Search Results")
                else:
                    console.print("[bold red]✖ Product is not found!![/bold red]\n")
        
        case 6:
            console.print("[bold red]Exiting the system... Goodbye![/bold red]")
            break
        
        case _:
            console.print("[bold red]Please enter a number between 1 to 6[/bold red]")