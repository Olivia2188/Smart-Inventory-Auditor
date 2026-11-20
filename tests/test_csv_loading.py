import unittest
from io import StringIO
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

from inventory import Inventory
from supplier import Supplier
from csv_loader import load_products


class TestCSVLoading(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.supplier = Supplier(
            "S001", "ABC Electronics", "abc@email.com"
        )

    def test_load_valid_products(self):
        output = StringIO()
        csv_path = Path(__file__).resolve().parent.parent / "products.csv"

        with redirect_stdout(output):
            load_products(str(csv_path), self.inventory, self.supplier)

        self.assertEqual(len(self.inventory.get_products()), 3)
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Skipping row 4", output.getvalue())
        self.assertIn("Skipping row 5", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())

    def test_missing_file(self):
        output = StringIO()

        with TemporaryDirectory() as folder:
            missing_path = Path(folder) / "missing.csv"

            with redirect_stdout(output):
                load_products(str(missing_path), self.inventory, self.supplier)

        self.assertIn("Products file not found:", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())
        self.assertEqual(len(self.inventory.get_products()), 0)


if __name__ == "__main__":
    unittest.main()
