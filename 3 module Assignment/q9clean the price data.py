
raw_prices = ["₹1,200", "₹850", "₹2,300", "₹1,750"]

clean_prices = []

for price in raw_prices:
    cleaned = price.replace("₹", "").replace(",", "")
    clean_prices.append(int(cleaned))

total = sum(clean_prices)
average = total / len(clean_prices)

print(f"Clean prices: {clean_prices}")
print(f"Total: ₹{total:.2f}")
print(f"Average: ₹{average:.2f}")