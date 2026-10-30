import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )
            
            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                print("Unknown product type. Skipping product.")
                continue

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.json not found.")

    return inventory

def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        product_data = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }

        if isinstance(product, PhysicalProduct):
            product_data["type"] = "physical"
            product_data["weight"] = product.get_weight()

        elif isinstance(product, DigitalProduct):
            product_data["type"] = "digital"
            product_data["download_size"] = product.get_download_size()

        data.append(product_data)

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")

inventory = load_inventory()

while True:
    print("====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("====================================")
    print("----------------MENU----------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------------------------")

    option = input("Enter option: ")
    
    if option == "1":
        inventory.display_all()

    elif option == "2":
        print("\nSelect Product Type:")
        print("1. Physical Product")
        print("2. Digital Product")

        product_type = input("Enter product type (1 or 2): ")

        if product_type not in ("1", "2"):
            print("Invalid product type! Please enter 1 or 2.")
            continue

        product_id = input("Product ID: ").upper()
        name = input("Product Name: ")
        price = float(input("Product Price: "))
        stock = int(input("Stock Quantity: "))

        if product_type == "1":
            weight = float(input("Weight (kg): "))
            new_product = PhysicalProduct(
                product_id, name, price, stock, weight
            )

        elif product_type == "2":
            download_size = float(input("Download Size (MB): "))
            new_product = DigitalProduct(
                product_id, name, price, stock, download_size
            )

        inventory.add_product(new_product)
        print("Product added successfully!")

    elif option == "3":
        product_id = input("Enter Product ID: ").upper()
        product = inventory.search_product(product_id)

        if product is not None:
            new_stock = int(input("New Stock Quantity: "))
            product.update_stock(new_stock)
            print("Stock updated successfully!")

        else:
            print("Product not found.")

    elif option == "4":
        product_id = input("Enter Product ID: ").upper()
        product = inventory.search_product(product_id)

        if product is not None:
            print("Product Found: ")
            product.display_information()

        else:
            print("Product not found")

    elif option == "5":
        save_inventory(inventory)

    elif option == "6":
        save_inventory(inventory)
        print("Program terminated.")
        break

    else: 
        print("Invalid option. Please try again.")
