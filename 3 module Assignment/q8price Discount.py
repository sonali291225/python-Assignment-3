
prices = [250, 1200, 480, 999, 3500, 150]

discounted = [price * 0.90 for price in prices]

above_500 = [price for price in prices if price > 500]

before_total = sum(prices)
after_total = sum(discounted)

print(f"Discounted prices: {discounted}")
print(f"Original prices above 500: {above_500}")
print(f"Before discount: ₹{before_total:.2f}")
print(f"After discount: ₹{after_total:.2f}")