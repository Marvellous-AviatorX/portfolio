"""
💳 Credit Card Validator (Luhn Algorithm)
-----------------------------------------
This program checks if a given credit card number is valid using the Luhn algorithm:
✅ Reverses the digits
✅ Doubles every second digit
✅ Subtracts 9 from numbers greater than 9
✅ Sums all digits
✅ Validates if the sum is divisible by 10

If divisible by 10 ➝ The card number is VALID ✅
Else ➝ The card number is INVALID ❌
"""

no = input("🔢 Enter a 16-digit credit card number: ")

# Reverse the number into a list
rev_no = list(no[::-1])
add = 0
print(f"🔄 Reversed digits: {rev_no}")

# ✅ Step 1: Check length
if len(no) != 16:
    print("❌ Non valid: Card number must be 16 digits")
else:
    # ✅ Step 2: Double every second digit
    for a in range(1, len(rev_no), 2):
        rev_no[a] = int(rev_no[a]) * 2
        print(f"➡️ After doubling every 2nd digit: {rev_no}")

    # ✅ Step 3: Subtract 9 from numbers greater than 9
    for b in range(0, len(rev_no)):
        rev_no[b] = int(rev_no[b])
        if rev_no[b] > 9:
            rev_no[b] -= 9

    print(f"📉 After subtracting 9 from values > 9: {rev_no}")

    # ✅ Step 4: Sum all digits
    for c in range(0, len(rev_no)):
        add += int(rev_no[c])

    print(f"➕ Total sum of digits = {add}")

    # ✅ Step 5: Validate
    if (add % 10) == 0:
        print("✅ VALID credit card number")
    else:
        print("❌ NON valid credit card number")
