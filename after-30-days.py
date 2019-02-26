from classes.CarInsurance import CarInsurance
from classes.Product import Product
from classes.products.FullCoverage import FullCoverage
from classes.products.LowCoverage import LowCoverage
from classes.products.MegaCoverage import MegaCoverage
from classes.products.SpecialFullCoverage import SpecialFullCoverage
from classes.products.SuperSale import SuperSale
from classes.products.MediumCoverage import MediumCoverage


productsAtDayZero = [
    MediumCoverage('Medium Coverage', 10, 20),
    FullCoverage('Full Coverage', 2, 0),
    LowCoverage('Low Coverage', 5, 7),
    MegaCoverage('Mega Coverage', 0, 80),
    MegaCoverage('Mega Coverage', -1, 80),
    SpecialFullCoverage('Special Full Coverage', 15, 20),
    SpecialFullCoverage('Special Full Coverage', 10, 49),
    SpecialFullCoverage('Special Full Coverage', 5, 49),
    SuperSale('Super Sale', 3, 6),
]

carInsurance = CarInsurance(productsAtDayZero)

carInsurance.makeFile()