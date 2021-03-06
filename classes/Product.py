class Product():

    def __init__(self, name, sellIn, price):
        self.name = name
        self.sellIn = sellIn
        self.price = price

    def updatePrice(self):
        deg = 1
        if self.sellIn < 1:
            deg = 2
        self.price = max(0, min(50, self.price - deg))

    def updateSellIn(self):
        self.sellIn = self.sellIn - 1

    def updateValues(self):
        self.updatePrice()
        self.updateSellIn()