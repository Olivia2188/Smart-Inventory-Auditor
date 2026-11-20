import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header

            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError("Invalid number of columns.")

                    product_type, product_id, name, price, stock = row

                    price = float(price)
                    stock = int(stock)

                    # The sample CSV does not include these fields
                    weight = 0.0 if product_type == "physical" else None
                    download_size = 0.0 if product_type == "digital" else None

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        price,
                        stock,
                        supplier,
                        weight=weight,
                        download_size=download_size
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")
