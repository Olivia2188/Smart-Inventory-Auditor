from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

supplier = Supplier("S001", "ABC Electronics", "contact@abc.com")

laptop = PhysicalProduct(
    "P001", "Laptop", 1200.0, 15, 2.5, supplier
)

software = DigitalProduct(
    "D001", "Software", 49.99, 100, 500, supplier
)

print("Testing PhysicalProduct:")
show_product_details(laptop)

print("\nTesting DigitalProduct:")
show_product_details(software)

inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(software)

print("\nTesting Inventory:")
inventory.display_all()

print("\nTesting Polymorphism")

for product in inventory.get_products():
    product.display_information
    print(product.get_fulfilment_info())
    print()