
sales = [
    ("Phone", 18000),
    ("Laptop", 55000),
    ("Phone", 17500),
    ("Mouse", 700),
    ("Laptop", 52000),
    ("Mouse", 650)
]

totals = {}


for category, amount in sales:
    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

best_category = max(totals, key=totals.get)

print(f"Category totals: {totals}")
print(f"Highest category: {best_category}")
print(f"Highest total: ₹{totals[best_category]}")