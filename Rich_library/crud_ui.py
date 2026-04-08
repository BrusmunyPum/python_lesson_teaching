import csv
from pathlib import Path
from typing import Any, Dict, List, Optional

from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.prompt import Confirm, FloatPrompt, IntPrompt, Prompt
from rich.table import Table
from rich.text import Text

console = Console()

FILE_PATH = Path("products_data.csv")
EXPORT_DIR = Path("exports")
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
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    if not FILE_PATH.exists():
        save_products(DEFAULT_PRODUCTS)
        show_success("Created sample CSV data file.")


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


def stock_status(qty: int) -> str:
    if qty <= 0:
        return "Out of Stock"
    if qty <= 10:
        return "Low Stock"
    return "In Stock"


def stock_style(qty: int) -> str:
    if qty <= 0:
        return "bold red"
    if qty <= 10:
        return "bold yellow"
    return "bold green"


def total_inventory_value(products: List[Product]) -> float:
    return sum(product["pqty"] * product["price"] for product in products)


def show_header() -> None:
    title = Text("PRODUCT MANAGEMENT CONSOLE", style="bold white")
    console.print(
        Panel(
            Align.center(Group(title)),
            border_style="bright_blue",
            box=box.DOUBLE,
            padding=(1, 2),
        )
    )


def show_success(message: str) -> None:
    console.print(f"[bold green]✓ {message}[/bold green]")


def show_warning(message: str) -> None:
    console.print(f"[bold yellow]! {message}[/bold yellow]")


def show_error(message: str) -> None:
    console.print(f"[bold red]✗ {message}[/bold red]")


def pause() -> None:
    Prompt.ask("\n[dim]Press Enter to continue[/dim]", default="")


def find_product_by_id(products: List[Product], pid: int) -> Optional[Product]:
    for product in products:
        if product["pid"] == pid:
            return product
    return None


def build_dashboard(products: List[Product]) -> Panel:
    categories = sorted({p["pcat"] for p in products})
    total_items = len(products)
    total_qty = sum(p["pqty"] for p in products)
    low_stock = sum(1 for p in products if 0 < p["pqty"] <= 10)
    out_stock = sum(1 for p in products if p["pqty"] == 0)
    total_value = total_inventory_value(products)

    cards = [
        Panel(f"[bold cyan]{total_items}[/bold cyan]\nProducts", border_style="cyan", box=box.ROUNDED),
        Panel(f"[bold green]{total_qty}[/bold green]\nUnits", border_style="green", box=box.ROUNDED),
        Panel(f"[bold yellow]{low_stock}[/bold yellow]\nLow Stock", border_style="yellow", box=box.ROUNDED),
        Panel(f"[bold red]{out_stock}[/bold red]\nOut of Stock", border_style="red", box=box.ROUNDED),
        Panel(f"[bold magenta]${total_value:,.2f}[/bold magenta]\nInventory Value", border_style="magenta", box=box.ROUNDED),
        Panel(
            f"[bold white]{', '.join(categories) if categories else '-'}[/bold white]\nCategories",
            border_style="bright_blue",
            box=box.ROUNDED,
        ),
    ]
    return Panel(Columns(cards, expand=True), title="[bold bright_cyan]Dashboard[/bold bright_cyan]", border_style="bright_blue")


def render_products_table(products: List[Product], title: str = "Products") -> None:
    if not products:
        console.print(Panel("[yellow]No products found.[/yellow]", border_style="yellow"))
        return

    table = Table(
        title=title,
        box=box.ROUNDED,
        header_style="bold white on blue",
        show_lines=True,
        expand=True,
    )
    table.add_column("ID", style="bold cyan", justify="center")
    table.add_column("Product Name", style="bold white", justify="center")
    table.add_column("Category", style="bold magenta", justify="center")
    table.add_column("Qty", style="bold green", justify="center")
    table.add_column("Price", style="bold yellow", justify="center")
    table.add_column("Value", style="bold cyan", justify="center")
    table.add_column("Status", style="bold", justify="center")

    for product in products:
        qty = product["pqty"]
        table.add_row(
            str(product["pid"]),
            product["pname"],
            product["pcat"],
            str(qty),
            f"${product['price']:,.2f}",
            f"${product['price'] * qty:,.2f}",
            f"[{stock_style(qty)}]{stock_status(qty)}[/{stock_style(qty)}]",
        )

    console.print(table)


def export_products_report(products: List[Product], file_name: str = "inventory_report.csv") -> Path:
    export_path = EXPORT_DIR / file_name
    with open(export_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES + ["stock_status", "inventory_value"])
        writer.writeheader()
        for product in products:
            row = dict(product)
            row["stock_status"] = stock_status(product["pqty"])
            row["inventory_value"] = round(product["pqty"] * product["price"], 2)
            writer.writerow(row)
    return export_path


def main_menu() -> str:
    console.print(
        Panel(
            "[bold cyan]1[/bold cyan]  Add Product\n"
            "[bold cyan]2[/bold cyan]  View Products\n"
            "[bold cyan]3[/bold cyan]  Update Product\n"
            "[bold cyan]4[/bold cyan]  Delete Product\n"
            "[bold cyan]5[/bold cyan]  Search Product\n"
            "[bold cyan]6[/bold cyan]  Export Report\n"
            "[bold cyan]7[/bold cyan]  Exit",
            title="[bold bright_white]Main Menu[/bold bright_white]",
            border_style="cyan",
            box=box.ROUNDED,
        )
    )
    return Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6", "7"], default="2")


def add_product() -> None:
    products = load_products()
    console.print(Panel.fit("[bold green]Add New Product[/bold green]", border_style="green"))

    pid = IntPrompt.ask("Product ID")
    if find_product_by_id(products, pid):
        show_error("A product with this ID already exists.")
        return

    pname = Prompt.ask("Product Name").strip()
    pqty = IntPrompt.ask("Quantity", default=0)
    pcat = Prompt.ask("Category").strip()
    price = FloatPrompt.ask("Price", default=0.0)

    products.append({
        "pid": pid,
        "pname": pname,
        "pqty": pqty,
        "pcat": pcat,
        "price": price,
    })
    save_products(products)
    show_success("Product added successfully.")


def view_products() -> None:
    while True:
        products = load_products()
        console.print(
            Panel(
                "[bold]1.[/bold] View All Products\n"
                "[bold]2.[/bold] Filter by Name\n"
                "[bold]3.[/bold] Filter by Category\n"
                "[bold]4.[/bold] Filter by Exact Price\n"
                "[bold]5.[/bold] Show Low Stock Only\n"
                "[bold]6.[/bold] Back",
                title="[bold bright_blue]View Menu[/bold bright_blue]",
                border_style="bright_blue",
            )
        )
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6"], default="1")

        if choice == "1":
            render_products_table(products, "All Products")
            pause()
        elif choice == "2":
            keyword = Prompt.ask("Enter product name").lower().strip()
            filtered = [p for p in products if keyword in p["pname"].lower()]
            render_products_table(filtered, f"Products matching name: {keyword}")
            pause()
        elif choice == "3":
            keyword = Prompt.ask("Enter category").lower().strip()
            filtered = [p for p in products if keyword in p["pcat"].lower()]
            render_products_table(filtered, f"Products in category: {keyword}")
            pause()
        elif choice == "4":
            price = FloatPrompt.ask("Enter exact price")
            filtered = [p for p in products if p["price"] == price]
            render_products_table(filtered, f"Products with price: ${price:,.2f}")
            pause()
        elif choice == "5":
            filtered = [p for p in products if p["pqty"] <= 10]
            render_products_table(filtered, "Low Stock Products")
            pause()
        else:
            break


def update_product() -> None:
    products = load_products()
    pid = IntPrompt.ask("Enter product ID to update")
    product = find_product_by_id(products, pid)

    if not product:
        show_error("Product not found.")
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

        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6"], default="6")

        if choice == "1":
            product["pname"] = Prompt.ask("New name", default=product["pname"]).strip()
            show_success("Name updated.")
        elif choice == "2":
            product["pqty"] = IntPrompt.ask("New quantity", default=product["pqty"])
            show_success("Quantity updated.")
        elif choice == "3":
            product["pcat"] = Prompt.ask("New category", default=product["pcat"]).strip()
            show_success("Category updated.")
        elif choice == "4":
            product["price"] = FloatPrompt.ask("New price", default=product["price"])
            show_success("Price updated.")
        elif choice == "5":
            product["pname"] = Prompt.ask("New name", default=product["pname"]).strip()
            product["pqty"] = IntPrompt.ask("New quantity", default=product["pqty"])
            product["pcat"] = Prompt.ask("New category", default=product["pcat"]).strip()
            product["price"] = FloatPrompt.ask("New price", default=product["price"])
            show_success("Product updated.")
        else:
            save_products(products)
            show_success("Changes saved successfully.")
            break


def delete_product() -> None:
    products = load_products()
    pid = IntPrompt.ask("Enter product ID to delete")
    product = find_product_by_id(products, pid)

    if not product:
        show_error("Product not found.")
        return

    render_products_table([product], "Product to Delete")
    if Confirm.ask("Are you sure you want to delete this product?", default=False):
        products = [p for p in products if p["pid"] != pid]
        save_products(products)
        show_success("Product deleted successfully.")
    else:
        show_warning("Delete cancelled.")


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
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"], default="2")

        if choice == "1":
            pid = IntPrompt.ask("Enter product ID")
            product = find_product_by_id(products, pid)
            render_products_table([product] if product else [], f"Search Result for ID: {pid}")
            pause()
        elif choice == "2":
            keyword = Prompt.ask("Enter product name").lower().strip()
            matches = [p for p in products if keyword in p["pname"].lower()]
            render_products_table(matches, f"Search Result for Name: {keyword}")
            pause()
        elif choice == "3":
            keyword = Prompt.ask("Enter category").lower().strip()
            matches = [p for p in products if keyword in p["pcat"].lower()]
            render_products_table(matches, f"Search Result for Category: {keyword}")
            pause()
        elif choice == "4":
            price = FloatPrompt.ask("Enter product price")
            matches = [p for p in products if p["price"] == price]
            render_products_table(matches, f"Search Result for Price: ${price:,.2f}")
            pause()
        else:
            break


def export_report() -> None:
    products = load_products()
    file_name = Prompt.ask("Export file name", default="inventory_report.csv").strip()
    if not file_name.lower().endswith(".csv"):
        file_name += ".csv"
    path = export_products_report(products, file_name=file_name)
    show_success(f"Report exported to: {path}")


def run() -> None:
    ensure_data_file()

    while True:
        console.clear()
        products = load_products()
        show_header()
        console.print(build_dashboard(products))
        console.print()
        try:
            option = main_menu()
            console.print()
            if option == "1":
                add_product()
            elif option == "2":
                view_products()
            elif option == "3":
                update_product()
            elif option == "4":
                delete_product()
            elif option == "5":
                search_products()
            elif option == "6":
                export_report()
            elif option == "7":
                console.print(
                    Panel.fit(
                        "[bold cyan]Thanks for using the Product Management Console.[/bold cyan]\n"
                        "[white]Goodbye and happy coding![/white]",
                        border_style="cyan",
                    )
                )
                break
            pause()
        except KeyboardInterrupt:
            console.print("\n[bold red]Application interrupted by user.[/bold red]")
            break
        except Exception as exc:
            show_error(f"Unexpected error: {exc}")
            pause()


if __name__ == "__main__":
    run()
