sales = {
    "Aman": 5400,
    "Pooja": 2300,
    "Rahul": 800,
    "Neha": 6100
}
star_count = 0

for name, amount in sales.items():
    if amount >= 5000:
        rating = "Star"
        star_count += 1
    elif amount >= 2000:
        rating = "Good"
    else:
        rating = "Needs Improvement"

    print(f"{name}: {rating}")

print(f"Total Star salespeople: {star_count}")