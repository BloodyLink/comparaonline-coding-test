from ..Product import Product

class SuperSale(Product):

    def updatePrice(self):
        inc = 2
        if self.sellIn < 1:
            inc = 4
        self.price = max(0, min(50, self.price - inc))