import unittest
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)


class TestStrategy(unittest.TestCase):

    def setUp(self):
        supplier = Supplier(
            "S001", "ABC Electronics", "abc@email.com"
        )

        product = PhysicalProduct(
            "P001", "Monitor", 250.0, 10, 3.0, supplier
        )

        self.order = Order("O001")
        self.order.add_order_line(product, 1)

    def test_no_discount(self):
        self.assertEqual(self.order.calculate_total(), 250.0)

    def test_percentage_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.calculate_total(), 225.0)

    def test_bulk_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230.0)

    def test_student_discount(self):
        self.order.set_discount(StudentDiscount())
        self.assertEqual(self.order.calculate_total(), 237.5)

    def test_change_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230.0)

        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.calculate_total(), 225.0)


if __name__ == "__main__":
    unittest.main()
