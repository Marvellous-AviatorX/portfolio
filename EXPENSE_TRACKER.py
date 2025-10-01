"""
📝 Budget & Expense Tracker Program
-----------------------------------
This program allows you to:
✅ Enter your planned budget
✅ Add multiple expenses with item names and amounts
✅ Automatically calculate the total expenses
✅ Show your remaining balance after expenses
✅ Display all expenses in a neat format with emojis for fun 🎉

Perfect for personal budgeting, small businesses, or students 
who want to keep track of spending 💰.
"""

Budget = float(input("💰 Enter your planned budget: "))

Expense = []
total = 0

while True:
    name = input("🛒 Enter the name of the item (or type 'done' if finished): ")
    if name.lower() == "done":
        break
    amount = int(input(f"💵 Enter amount for {name}: "))
    Expense.append((name, amount))

for name, amount in Expense:
    total += amount

updated_balance = Budget - total

print("\n📊 Total expenses with amounts are as follows:")
for name, amount in Expense:
    print(f"➡️ {name}: {amount:.2f} 🧾")

print(f"\n💸 Total amount spent is: {total:.2f}")
print(f"✅ Remaining balance is: {updated_balance:.2f}")
