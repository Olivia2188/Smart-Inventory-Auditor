from supplier import Supplier
from product_factory import ProductFactory


supplier = Supplier("S001", "ABC Electronics", "abc@email.com")

physical = ProductFactory.create(
    "physical", "P001", "Laptop", 1200.0, 10,
    supplier, weight=2.5
)

digital = ProductFactory.create(
    "digital", "D001", "Software", 49.99, 100,
    supplier, download_size=500
)

print("Testing Physical Product:")
physical.display_information()

print("\nTesting Digital Product:")
digital.display_information()

print("\nTesting Unknown Product Type:")

try:
    unknown = ProductFactory.create(
        "service", "S001", "Installation", 30.0, 5, supplier
    )
except ValueError as error:
    print("Error:", error)
