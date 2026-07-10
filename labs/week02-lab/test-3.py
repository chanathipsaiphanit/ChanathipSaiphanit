print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input

weight_input = float(input(" weight (kg) : "))
height_input = float(input(" height (m) : "))

#process

bmi = weight_input / (height_input ** 2)

#output

print("BMI = ",bmi)