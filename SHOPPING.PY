print("👋 Goodday and welcome to our company! \n")
name = input("📝 What is your name? \n")
age = int(input("What is your age?\n"))

menu = ["\n1.🍞 Bread",
"2.🥤 Coke",
"3.🍰 Cake"]
bread = 150
coke = 250
cake = 200

item = input("🛒 What item do you want to get from the menu? \n")
print("\n".join(menu))
if item.lower() == "bread":
    cost = bread
elif item.lower() == "coke":
    cost = coke
elif item.lower() == "cake":
    cost = cake
else:
    print("⚠ Item unavailable ❌")

item_quantity = int(input("🔢 How many do you want to get? \n"))
total_cost = item_quantity * cost
discount = ((20/100) * total_cost)

if age < 18:
    print("🚫 The presence of an adult is needed to buy")
elif total_cost > 750:
    print("💰 Cost is " + str(total_cost) + " without discount \n")
    print("✅ Final cost is " + str(total_cost - discount))