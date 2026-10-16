# Simple Stock Tracker
# Internship Project

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("================================")
print("       STOCK TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you have finished adding stocks.")

while True:
    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name == "DONE":
        break

    # Check whether stock exists
    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    # Get quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Calculate investment
    price = stock_prices[stock_name]
    investment = price * quantity

    # Store investment details
    portfolio.append({
        "stock": stock_name,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    total_investment += investment

    print(f"{stock_name}: {quantity} shares × ${price} = ${investment}")


# Display portfolio
print("\n================================")
print("       INVESTMENT SUMMARY")
print("================================")

if not portfolio:
    print("No stocks were added.")
else:
    for item in portfolio:
        print(
            f"{item['stock']} | "
            f"Price: ${item['price']} | "
            f"Quantity: {item['quantity']} | "
            f"Value: ${item['investment']}"
        )

    print("--------------------------------")
    print(f"Total Investment: ${total_investment}")


# Save result to a text file
save_file = input("\nDo you want to save the report? (yes/no): ").lower()

if save_file == "yes":
    with open("stock_report.txt", "w") as file:
        file.write("STOCK INVESTMENT REPORT\n")
        file.write("=======================\n\n")

        for item in portfolio:
            file.write(
                f"{item['stock']} | "
                f"Price: ${item['price']} | "
                f"Quantity: {item['quantity']} | "
                f"Value: ${item['investment']}\n"
            )

        file.write("\n-----------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Report saved successfully as 'stock_report.txt'.")

print("\nThank you for using Stock Tracker!")
