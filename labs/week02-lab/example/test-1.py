print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

#input
radius = input("Radius :")
radius = float(radius)


#process
area = 3.14159 * radius **2
circumference = 2 * 3.14159 * radius


#output
print("Calculate area:",area)
print("circumference:"+str(circumference))