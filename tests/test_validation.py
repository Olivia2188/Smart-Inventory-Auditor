import unittest
from supplier import Supplier
from physical_product import PhysicalProduct
from order_line import OrderLine


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Electronics", "abc@email.com"
        )

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P001", "Laptop", -100, 10, 2.5, self.supplier
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P001", "Laptop", 1200, -5, 2.5, self.supplier
            )

    def test_update_negative_stock(self):
        product = PhysicalProduct(
            "P001", "Laptop", 1200, 10, 2.5, self.supplier
        )

        with self.assertRaises(ValueError):
            product.update_stock(-5)

        self.assertEqual(product.get_stock(), 10)

    def test_invalid_order_quantity(self):
        product = PhysicalProduct(
            "P001", "Laptop", 1200, 10, 2.5, self.supplier
        )

        with self.assertRaises(ValueError):
            OrderLine(product, 0)

    def test_valid_order_quantity(self):
        product = PhysicalProduct(
            "P001", "Laptop", 1200, 10, 2.5, self.supplier
        )

        order_line = OrderLine(product, 2)
        self.assertEqual(order_line.calculate_subtotal(), 2400)


if __name__ == "__main__":
    unittest.main()
