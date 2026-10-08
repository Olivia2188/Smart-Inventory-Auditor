import json

inventory = [
    {
        "id": "P001",      # product 1
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",     # product 2
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",       # product 3
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

def display_all(items):
    print("Current Inventory")
    print("---------------------------")

    for product in items:
        print(
            f"ID: {product['id']}  | "
            f"Name:{product['name']}   | " 
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("----------------------------")

def add_product(items):
    print("Add New Product")

    product_id = input("Product ID:")
    product_name = input("Product Name:")
    product_price = float(input("Price:"))
    product_stock = int(input("Number of stock:"))

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "stock":product_stock
    }

    items.append(new_product)

    print("Product added successfully")

def update_stock(items):
    print ("Update Stock")

    while True:
        product_id = input("Enter Product ID:")

        for product in items:
            if product["id"] == product_id:
                print("Product Found:")
                print("Name:", product["name"])
                print("Current Stock:", product["stock"])

                new_stock = int(input("New Stock Quantity: "))
                product["stock"] = new_stock

                print("Stock updated successfully!")
                display_all(items)
                return

        print("Product not found.")

def search_product(items):
    print("Search Product")

    while True:
        product_id = input("Enter Product ID: ")

        for product in items:
            if product["id"] == product_id:
                print("Product Found")
                print("-----------------------------------")
                print("ID:", product["id"])
                print("Name:", product["name"])
                print(f"Price: ${product['price']:.2f}")
                print("Stock:", product["stock"])
                print("-----------------------------------")
                return

        print("Product not found.")

def load_inventory():
    try:
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except FileNotFoundError:
        print("inventory.json not found")
        return []

def save_inventory(inventory):
    file = open("inventory.json", "w")

    json.dump(inventory, file, indent=4)

    file.close()

    print("Inventory saved successfully to inventory.json.")

inventory = load_inventory()

while True:
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================")
    print("--------------MENU----------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------------")

    option = input("Enter option: ")

    if option == "1":
        display_all(inventory)

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        search_product(inventory)

    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    
    else:
        print("Invalid option. Please try again.")


