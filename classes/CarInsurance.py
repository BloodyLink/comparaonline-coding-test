class CarInsurance():

    def __init__(self, products):
        self.products = products

    def updateValues(self):
        for product in self.products:
            product.updateValues()
            
    # def productPrinter(self, products):
    #     for product in products:
    #         with open('products_after_30_days.txt', 'a+') as file:
    #             file.write(f'{product.name}, {product.sellIn}, {product.price}\n')

    def makeFile(self):

        # Day 0
        with open('products_after_30_days.txt', 'w+') as file:
                file.write(f'\n-------- day 0 --------\n')
                file.write('name, sellIn, price\n')
                for product in self.products:
                    file.write(f'{product.name}, {product.sellIn}, {product.price}\n')
                # self.productPrinter(self.products)
                file.write('\n')

        # Days 1 to 30
        for day in range(1, 31):
            self.updateValues()
            with open('products_after_30_days.txt', 'a+') as file:
                file.write(f'-------- day {day} --------\n')
                file.write('name, sellIn, price\n')
                for product in self.products:
                    file.write(f'{product.name}, {product.sellIn}, {product.price}\n')
                file.write('\n')