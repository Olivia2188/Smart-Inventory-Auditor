from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

supplier = Supplier("S001", "ABC Electronics", "contact@abc.com")

laptop = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)
software = DigitalProduct("D001", "Software", 49.99, 100, 500, supplier)

print("Before deleting supplier variable:")
laptop.get_supplier().display_information()

del supplier

print("\nAfter deleting supplier variable:")
laptop.get_supplier().display_information()
software.get_supplier().display_information()

