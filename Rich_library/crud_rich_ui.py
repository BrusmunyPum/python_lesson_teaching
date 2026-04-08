import csv
from pathlib import Path
from typing import List, Dict, Any, Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm
from rich import box

console = Console()

FILE_PATH = Path("File_IO/products_data.csv")
FIELDNAMES = ["pid", "pname", "pqty", "pcat", "price"]

DEFAULT_PRODUCTS = [
    {"pid": 101, "pname": "Laptop", "pqty": 15, "pcat": "Electronics", "price": 899.99},
    {"pid": 102, "pname": "Wireless Mouse", "pqty": 50, "pcat": "Electronics", "price": 25.50},
    {"pid": 103, "pname": "Mechanical Keyboard", "pqty": 30, "pcat": "Electronics", "price": 75.00},
    {"pid": 104, "pname": "Coffee Maker", "pqty": 12, "pcat": "Home Goods", "price": 45.99},
    {"pid": 105, "pname": "Desk Lamp", "pqty": 40, "pcat": "Home Goods", "price": 18.25},
    {"pid": 106, "pname": "Office Chair", "pqty": 8, "pcat": "Furniture", "price": 120.00},
    {"pid": 107, "pname": "Water Bottle", "pqty": 100, "pcat": "Accessories", "price": 12.50},
    {"pid": 108, "pname": "Backpack", "pqty": 25, "pcat": "Accessories", "price": 55.00},
    {"pid": 109, "pname": "Smartphone", "pqty": 20, "pcat": "Electronics", "price": 699.00},
    {"pid": 110, "pname": "Notebook", "pqty": 200, "pcat": "Stationery", "price": 4.99},
]


Product = Dict[str, Any]


def ensure_data_file() -> None:
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not FILE_PATH.exists():
        save_products(DEFAULT_PRODUCTS)
        console.print("[bold green]Created sample data file successfully.[/bold green]")



def load_products() -> List[Product]:
    ensure_data_file()
    products: List[Product] = []
    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["pid"] = int(row["pid"])
            row["pqty"] = int(row["pqty"])
            row["price"] = float(row["price"])
            products.append(row)
    return products



def save_products(products: List[Product]) -> None:
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(products)



def show_header() -> None:
    console.print(
        Panel.fit(
            "[bold cyan]Product Management System[/bold cyan]\n"
            "[white]Modern CRUD console with [bold magenta]Rich[/bold magenta][/white]",
            border_style="bright_blue",
            padding=(1, 4),
        )
    )



def show_message(message: str, style: str = "green") -> None:
    console.print(f"[bold {style}]{message}[/bold {style}]")



def find_product_by_id(products: List[Product], pid: int) -> Optional[Product]:
    for product in products:
        if product["pid"] == pid:
            return product
    return None



def render_products_table(products: List[Product], title: str = "Product List") -> None:
    if not products:
        console.print(Panel("[yellow]No products found.[/yellow]", border_style="yellow"))
        return

    table = Table(title=title, box=box.ROUNDED, header_style="bold white on blue", show_lines=False)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="bright_white")
    table.add_column("Category", style="magenta")
    table.add_column("Qty", style="green", justify="right")
    table.add_column("Price ($)", style="yellow", justify="right")
    table.add_column("Stock Status", justify="center")

    for product in products:
        qty = product["pqty"]
        if qty == 0:
            stock = "[bold red]Out[/bold red]"
        elif qty <= 10:
            stock = "[bold yellow]Low[/bold yellow]"
        else:
            stock = "[bold green]Good[/bold green]"

        table.add_row(
            str(product["pid"]),
            product["pname"],
            product["pcat"],
            str(product["pqty"]),
            f"{product['price']:.2f}",
            stock,
        )

    console.print(table)



def main_menu() -> int:
    console.print(
        Panel(
            "[bold]1.[/bold] Add Product\n"
            "[bold]2.[/bold] View Products\n"
            "[bold]3.[/bold] Update Product\n"
            "[bold]4.[/bold] Delete Product\n"
            "[bold]5.[/bold] Search Product\n"
            "[bold]6.[/bold] Exit",
            title="[bold bright_cyan]Main Menu[/bold bright_cyan]",
            border_style="cyan",
        )
    )
    return IntPrompt.ask("[bold white]Choose an option[/bold white]", choices=["1", "2", "3", "4", "5", "6"])



def add_product() -> None:
    products = load_products()
    console.print(Panel.fit("[bold green]Add New Product[/bold green]", border_style="green"))

    pid = IntPrompt.ask("Product ID")
    while True:
        if find_product_by_id(products, pid):
            show_message("A product with that ID already exists.", "red")
            pid = IntPrompt.ask("Please input id again: ")
        else:
            break

    pname = Prompt.ask("Product Name").strip()
    pqty = IntPrompt.ask("Quantity")
    pcat = Prompt.ask("Category").strip()
    price = FloatPrompt.ask("Price")

    products.append({"pid": pid, "pname": pname, "pqty": pqty, "pcat": pcat, "price": price})
    save_products(products)
    show_message("Product added successfully.")



def view_products() -> None:
    while True:
        products = load_products()
        console.print(
            Panel(
                "[bold]1.[/bold] View All\n"
                "[bold]2.[/bold] Filter by Name\n"
                "[bold]3.[/bold] Filter by Category\n"
                "[bold]4.[/bold] Filter by Exact Price\n"
                "[bold]5.[/bold] Back",
                title="[bold bright_blue]View Menu[/bold bright_blue]",
                border_style="bright_blue",
            )
        )
        choice = IntPrompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])

        if choice == 1:
            render_products_table(products, "All Products")
        elif choice == 2:
            keyword = Prompt.ask("Enter product name").lower().strip()
            filtered = [p for p in products if keyword in p["pname"].lower()]
            render_products_table(filtered, f"Products matching name: {keyword}")
        elif choice == 3:
            keyword = Prompt.ask("Enter category").lower().strip()
            filtered = [p for p in products if keyword in p["pcat"].lower()]
            render_products_table(filtered, f"Products in category: {keyword}")
        elif choice == 4:
            price = FloatPrompt.ask("Enter exact price")
            filtered = [p for p in products if p["price"] == price]
            render_products_table(filtered, f"Products with price: {price:.2f}")
        else:
            break



def update_product() -> None:
    products = load_products()
    pid = IntPrompt.ask("Enter product ID to update")
    product = find_product_by_id(products, pid)

    if not product:
        show_message("Product not found.", "red")
        return

    while True:
        render_products_table([product], "Selected Product")
        console.print(
            Panel(
                "[bold]1.[/bold] Update Name\n"
                "[bold]2.[/bold] Update Quantity\n"
                "[bold]3.[/bold] Update Category\n"
                "[bold]4.[/bold] Update Price\n"
                "[bold]5.[/bold] Update All\n"
                "[bold]6.[/bold] Save and Back",
                title="[bold yellow]Update Menu[/bold yellow]",
                border_style="yellow",
            )
        )

        choice = IntPrompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6"])

        if choice == 1:
            product["pname"] = Prompt.ask("New name").strip()
            show_message("Name updated.")
        elif choice == 2:
            product["pqty"] = IntPrompt.ask("New quantity")
            show_message("Quantity updated.")
        elif choice == 3:
            product["pcat"] = Prompt.ask("New category").strip()
            show_message("Category updated.")
        elif choice == 4:
            product["price"] = FloatPrompt.ask("New price")
            show_message("Price updated.")
        elif choice == 5:
            product["pname"] = Prompt.ask("New name").strip()
            product["pqty"] = IntPrompt.ask("New quantity")
            product["pcat"] = Prompt.ask("New category").strip()
            product["price"] = FloatPrompt.ask("New price")
            show_message("Product updated completely.")
        else:
            save_products(products)
            show_message("Changes saved successfully.")
            break



def delete_product() -> None:
    products = load_products()
    pid = IntPrompt.ask("Enter product ID to delete")
    product = find_product_by_id(products, pid)

    if not product:
        show_message("Product not found.", "red")
        return

    render_products_table([product], "Product to Delete")
    if Confirm.ask("Are you sure you want to delete this product?"):
        products = [p for p in products if p["pid"] != pid]
        save_products(products)
        show_message("Product deleted successfully.", "green")
    else:
        show_message("Delete cancelled.", "yellow")



def search_products() -> None:
    while True:
        products = load_products()
        console.print(
            Panel(
                "[bold]1.[/bold] Search by ID\n"
                "[bold]2.[/bold] Search by Name\n"
                "[bold]3.[/bold] Search by Category\n"
                "[bold]4.[/bold] Search by Exact Price\n"
                "[bold]5.[/bold] Back",
                title="[bold magenta]Search Menu[/bold magenta]",
                border_style="magenta",
            )
        )
        choice = IntPrompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])

        if choice == 1:
            pid = IntPrompt.ask("Enter product ID")
            product = find_product_by_id(products, pid)
            render_products_table([product] if product else [], f"Search Result for ID: {pid}")
        elif choice == 2:
            keyword = Prompt.ask("Enter product name").lower().strip()
            matches = [p for p in products if keyword in p["pname"].lower()]
            render_products_table(matches, f"Search Result for Name: {keyword}")
        elif choice == 3:
            keyword = Prompt.ask("Enter category").lower().strip()
            matches = [p for p in products if keyword in p["pcat"].lower()]
            render_products_table(matches, f"Search Result for Category: {keyword}")
        elif choice == 4:
            price = FloatPrompt.ask("Enter product price")
            matches = [p for p in products if p["price"] == price]
            render_products_table(matches, f"Search Result for Price: {price:.2f}")
        else:
            break



def run() -> None:
    show_header()
    ensure_data_file()

    while True:
        try:
            option = main_menu()
            if option == 1:
                add_product()
            elif option == 2:
                view_products()
            elif option == 3:
                update_product()
            elif option == 4:
                delete_product()
            elif option == 5:
                search_products()
            elif option == 6:
                console.print(Panel.fit("[bold cyan]Thanks for using the system. Goodbye![/bold cyan]", border_style="cyan"))
                break
        except KeyboardInterrupt:
            console.print("\n[bold red]Application interrupted by user.[/bold red]")
            break
        except Exception as exc:
            console.print(f"[bold red]Unexpected error:[/bold red] {exc}")


if __name__ == "__main__":
    run()
