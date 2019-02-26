from ..Product import Product

class SpecialFullCoverage(Product):

    def updatePrice(self):
        if self.sellIn > 10:
            self.price = max(0, min(50, self.price + 1))
        if self.sellIn <= 10 and self.sellIn > 5:
            self.price = max(0, min(50, self.price + 2))
        if self.sellIn <= 5:
            self.price = max(0, min(50, self.price + 3))
        if self.sellIn < 1:
            self.price = 0
        