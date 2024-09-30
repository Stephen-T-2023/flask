class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni

    def display(self):
        print(f"Pizza size: {self.size}")
        if self.cheese:
            print("Topping: Cheese")
        if self.pepperoni:
            print("Topping: Pepperoni")

class PizzaBuilder:
    def __init__(self):
        self.size = None 
        self.cheese = False
        self.pepperoni = False
    
    def set_size(self, size):
        self.size = size 
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def build(self):
        return Pizza(self.size , self.cheese , self.pepperoni)

builder = PizzaBuilder()
pizza = builder.set_size("Large").add_cheese().add_pepperoni().build()

pizza.display()