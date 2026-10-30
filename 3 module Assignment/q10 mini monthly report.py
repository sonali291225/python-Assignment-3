
sales = {
    "Jan": 4200,
    "Feb": 3900,
    "Mar": 5100,
    "Apr": 4700,
    "May": 5500
}

for month, amount in sales.items():
    bar = "*" * (amount // 100)
    print(f"{month}: ₹{amount} {bar}")

best_month = max(sales, key=sales.get)

total = sum(sales.values())

print(f"Best month: {best_month}")
print(f"Total sales: ₹{total}")