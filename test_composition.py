from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order

supplier = Supplier("S001", "ABC Electronics", "contact@abc.com")

laptop = PhysicalProduct(
    "P001", "Laptop", 1200.0, 15, 2.5, supplier
)

mouse = PhysicalProduct(
    "P002", "Mouse", 25.50, 40, 0.2, supplier
)

order_a = Order("ORD001")
order_a.add_order_line(laptop, 1)
order_a.add_order_line(mouse, 2)

print("Order A:")
for line in order_a.get_order_lines():
    print(
        line.get_product().get_name(),
        "x", line.get_quantity(),
        "Subtotal: $", f"{line.calculate_subtotal():.2f}"
    )

print(f"Order A Total: ${order_a.calculate_total():.2f}")

order_b = Order("ORD002")
order_b.add_order_line(laptop, 1)

print(f"\nOrder B Total: ${order_b.calculate_total():.2f}")

line_a = order_a.get_order_lines()[0]
line_b = order_b.get_order_lines()[0]

print("\nSame OrderLine object:", line_a is line_b)
print("Same Product object:", line_a.get_product() is line_b.get_product())

print("\nRemoving Laptop from Order A:")
order_a.remove_order_line(0)

print(f"Updated Order A Total: ${order_a.calculate_total():.2f}")

print("\nLaptop still exists:")
laptop.display_information()