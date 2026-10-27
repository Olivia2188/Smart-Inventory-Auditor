class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.apppend(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get__product_id() == product_id:
                return product

        return None

    def display_all(self):
        print("CUrrent Inventory")
        print("-------------------------------------")

        for product in self.__products:
            product.display_information()

        print("--------------------------------------")