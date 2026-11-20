import unittest
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


class TestFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Electronics", "abc@email.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Laptop", 1200.0,
            10, self.supplier, weight=2.5
        )

        self.assertIsInstance(product, PhysicalProduct)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Software", 49.99,
            100, self.supplier, download_size=500
        )

        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_product_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "S001", "Installation",
                30.0, 5, self.supplier
            )

    def test_missing_weight(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Mouse",
                25.0, 10, self.supplier
            )

    def test_missing_download_size(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital", "D002", "Antivirus",
                30.0, 50, self.supplier
            )


if __name__ == "__main__":
    unittest.main()
