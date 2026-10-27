import json

from product import Product
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

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

        data.append(product_data)

    file = open("inventory.json", "w")
    json.dump(data, file, indent=4)
    file.close()

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
        product_id = input("Product ID: ").upper()
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        new_product = Product(product_id, name, price, stock)
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
