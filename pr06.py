# Model this for JewelMind-style inventory:
# class Product:
#     - __init__(self, name, price, quantity)
#     - total_value() -> price * quantity
#     - __str__ -> "Name: <name>, Value: <total_value>"

# class JewelryItem(Product):
#     - adds: metal_type, weight_grams
#     - override total_value() -> (price * quantity) + (weight_grams * 50)  # extra cost factor
#     - override __str__ to also show metal_type

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Name: {self.name}, Value: {self.total_value()}"

class JewelryItem(Product):
    def __init__(self, name, price, quantity, metal_type, weight_grams):
        super().__init__(name, price, quantity)
        self.metal_type = metal_type
        self.weight_grams = weight_grams

    def total_value(self):
        return (self.price * self.quantity) + (self.weight_grams * 50)
    
    def __str__(self):
        return f"Name: {self.name}, Value: {self.total_value()}, Metal Type: {self.metal_type}"

j = JewelryItem("Gold Ring", 15000, 2, "Gold", 10)
print(j)
print(j.total_value())