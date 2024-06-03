class Product:
    def __init__(self, name:str, price:float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name:
                if amount > product.quantity:
                    return print(f"Sorry.You try to take {amount} {product.name} \n"
                                 f"But we have only {product.quantity} {product.name}.\n")

                product.quantity -= amount
                return print(f"You bought {amount} {product.name}\n")

        print(f"{product_name} not found in warehouse.\n")

    def __str__(self):
        print("At the moment, in the warehouse:")
        if self.products:
            product_strs = [str(product) for product in self.products]
            return "\n".join(product_strs)
        else:
            return "There are no products in warehouse.\n"


def main():
    inventory = Inventory()

    print(inventory)

    inventory.add_product(Product("Apple", 1.0, 10))
    inventory.add_product(Product("Banana", 0.5, 15))
    inventory.add_product(Product("Orange", 1.5, 8))

    print("Initial Inventory:")
    print(inventory)

    inventory.sell_product("Apple", 3)
    inventory.sell_product("Banana", 20)

    print("Updated Inventory:")
    print(inventory)


if __name__ == "__main__":
    main()
