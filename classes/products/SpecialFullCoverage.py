from ../Product import Product

class SpecialFullCoverage(Product):

    def updatePrice(self):
        inc = 1
        if self.sellIn <= 10:
            inc = 2
        elif self.sellIn <= 5:
            inc = 3    
        elif self.sellIn < 1:
            inc = self.price * (-1)
        return max(0, min(50, self.price + inc))