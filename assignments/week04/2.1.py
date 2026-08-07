
prices = []

print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))

total = 0
bought = []

for i in range(6):
    if total + prices[i] <= budget:
        print(f"Item {i+1} = {prices[i]} --> buy")
        total += prices[i]
        bought.append(prices[i])
    else:
        print(f"Item {i+1} = {prices[i]} --> cannot buy")

    print(f"Current total = {total}\n")
print(f"Bought items: {bought}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")