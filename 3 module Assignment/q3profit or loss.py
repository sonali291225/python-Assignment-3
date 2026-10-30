
products = {
    "Pen": [5, 8],
    "Book": [60, 55],
    "Bag": [400, 550],
    "Ruler": [10, 10]
}

for name, prices in products.items():
    cost = prices[0]
    selling = prices[1]

    difference = selling - cost

    if difference > 0:
        status = "Profit"
    elif difference < 0:
        status = "Loss"
    else:
        status = "No profit no loss"

    print(f"{name}: {status} = ₹{abs(difference)}")