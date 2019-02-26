from ..Product import Product

class FullCoverage(Product):

    def updatePrice(self):
        inc = 1
        if self.sellIn < 1:
            inc = 2
        return max(0, min(50, self.price + inc))