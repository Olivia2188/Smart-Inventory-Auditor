from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

supplier =  Supplier("S001", "ABC Electronics", "contact@abc.com")

laptop = PhysicalProduct(
    "P001", "Laptop", 1200.0, 15, 2.5, supplier
)

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(laptop) # Add laptop to Inventory A

print("Inventory A before removal:")
inventory_a.display_all()

inventory_a.remove_product("P001") # remove laptop from Inventory A

print("\nInventory A after removal:")
inventory_a.display_all()

print ("\nLaptop still exists:")  # check that laptop still exists
laptop.display_information()

inventory_b.add_product(laptop)   #Transfer laptop to Inventory B

print("\nInventory B after transfer:")
inventory_b.display_all()

print("\nSame object:", inventory_b.find_product("P001" is laptop))