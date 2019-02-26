from ..Product import Product

class MegaCoverage(Product):

    def updatePrice(self):
        self.price = 80

    def updateSellIn(self):
        self.sellIn = self.sellIn