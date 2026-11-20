from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import (NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount)

supplier = Supplier("S001", "ABC Electronics", "abc@email.com")

product = PhysicalProduct("P001", "Monitor", 250.0, 10, 3.0, supplier)

order = Order("O001")
order.add_order_line(product, 1)

print("No Discount:", order.calculate_total())

order.set_discount(BulkDiscount(200, 20))
print("Bulk Discount:", order.calculate_total())

order.set_discount(PercentageDiscount(10))
print("Percentage Discount:", order.calculate_total())

order.set_discount(StudentDiscount())
print("Student Discount:", order.calculate_total())
