"""
🛍️ Shopping Cart Program
--------------------------
This program allows users to:
✅ Add multiple items to a shopping cart with their costs
✅ Automatically calculate the total price
✅ Apply a 10% discount if the total price is above 5000 💸
✅ Display all purchased items with their costs
✅ Show both actual and discounted total prices 🎉

Perfect for small businesses or individuals 
who want to simulate purchases and discounts 🛒.
"""

cart = []  # List to store items and their costs
price = 0  # Variable to keep track of total price

# 🛒 Keep asking user for items until they type 'done'
while True:
    item = input("🛍️ Enter the item you want to get (or type 'done' to finish): ")
    if item.lower() == "done":
        break
    item_cost = float(input(f"💵 Enter the cost of {item}: "))
    cart.append((item, item_cost))  # Add item and its cost as a tuple

# 💰 Calculate the total price of items
for item, item_cost in cart:
    price += item_cost  

# 🎁 Apply discount if total is 5000 or more
if price >= 5000:
    print("🎉 Discount of 10% applied!")
    total_price = 0.9 * price
else:
    total_price = price

# 📊 Display results
print("\n🧾 Items purchased:")
for item, item_cost in cart:
    print(f"➡️ {item}: {item_cost:.2f}")

print(f"\n💸 The actual cost for the items bought is: {price:.2f}")
print(f"✅ The total cost including discount is: {total_price:.2f}")
