class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print("Name:",self.name)
        print("Price:",self.price)
pro1=Product("Car",200000)
pro2=Product("Mouse",5000)
pro1.display()
pro2.display()

