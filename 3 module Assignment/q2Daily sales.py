sales = [1200, 850, 2300, 1750, 990]
total = sum(sales)

average = total / len(sales)

highest = max(sales)
lowest = min(sales)

count = 0
for amount in sales:
    if amount > average:
        count += 1

print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Days above average: {count}")