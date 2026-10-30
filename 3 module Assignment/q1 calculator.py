
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total > 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_bill = total - discount

print(f"Total Amount: ₹{total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")