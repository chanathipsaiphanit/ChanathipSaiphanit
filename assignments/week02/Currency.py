print("1. Convert Thai Baht (THB) to US Dollars (USD)")
print("2. Convert US Dollars (USD) to Thai Baht (THB)")
 
choice = input("Choose conversion direction (1 or 2): ")
 
if choice == "1":
    thb = float(input("Enter amount in THB: "))
    usd = thb / 35.5
    print("Formula used: USD = THB / 35.5")
    print(f"Result: {usd:.2f} USD")
 
elif choice == "2":
    usd = float(input("Enter amount in USD: "))
    thb = usd * 35.5
    print("Formula used: THB = USD * 35.5")
    print(f"Result: {thb:.2f} THB")