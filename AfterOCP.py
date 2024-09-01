from abc import ABC, abstractmethod

# Interface untuk strategi diskon
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price):
        pass

# Diskon untuk produk elektronik
class ElectronicsDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return price * 0.10

# Diskon untuk produk pakaian
class ClothingDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return price * 0.20

# Diskon untuk produk kebutuhan sehari-hari
class GroceriesDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return price * 0.05

# Diskon baru untuk produk perhiasan
class JewelryDiscount(DiscountStrategy):
    def calculate_discount(self, price):
        return price * 0.15

# Kalkulator diskon setelah menerapkan OCP
class DiscountCalculator:
    def calculate_discount(self, discount_strategy, price):
        return discount_strategy.calculate_discount(price)

# Contoh penggunaan
calculator = DiscountCalculator()
electronics_discount = calculator.calculate_discount(ElectronicsDiscount(), 1000)
clothing_discount = calculator.calculate_discount(ClothingDiscount(), 500)
groceries_discount = calculator.calculate_discount(GroceriesDiscount(), 200)
jewelry_discount = calculator.calculate_discount(JewelryDiscount(), 800)

print(f"Electronics Discount: ${electronics_discount}")
print(f"Clothing Discount: ${clothing_discount}")
print(f"Groceries Discount: ${groceries_discount}")
print(f"Jewelry Discount: ${jewelry_discount}")
