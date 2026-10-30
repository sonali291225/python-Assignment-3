sales = [420, 390, 510, 470, 550, 600]

first_three = sales[:3]
last_three = sales[3:]

first_total = sum(first_three)
last_total = sum(last_three)

growth = (last_total - first_total) / first_total * 100

if growth > 0:
    print(f"Sales grew by {growth:.2f}%")
elif growth < 0:
    print(f"Sales fell by {abs(growth):.2f}%")
else:
    print("Sales remained the same")