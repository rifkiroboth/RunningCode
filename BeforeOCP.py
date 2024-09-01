class DiscountCalculator:
    def calculate_discount(self, product_type, price):
        if product_type == "electronics":
            return price * 0.10
        elif product_type == "clothing":
            return price * 0.20
        elif product_type == "groceries":
            return price * 0.05
        else:
            return 0

# Contoh penggunaan
calculator = DiscountCalculator()
electronics_discount = calculator.calculate_discount("electronics", 1000)
clothing_discount = calculator.calculate_discount("clothing", 500)
groceries_discount = calculator.calculate_discount("groceries", 200)

print(f"Electronics Discount: ${electronics_discount}")
print(f"Clothing Discount: ${clothing_discount}")
print(f"Groceries Discount: ${groceries_discount}")
