
visits = [
    "Aman", "Pooja", "Aman", "Rahul",
    "Neha", "Pooja", "Aman"
]

unique_customers = set(visits)
print(f"Unique customers: {unique_customers}")
print(f"Total unique customers: {len(unique_customers)}")

for name in unique_customers:
    count = visits.count(name)

    if count > 1:
        print(f"{name} visited {count} times")