weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
 
bmi = weight / (height * height)
 
print(f"Your BMI is: {bmi:.1f}")
 
if bmi < 18.5:
    print("BMI Category: Underweight")
elif bmi < 25.0:
    print("BMI Category: Normal weight")
elif bmi < 30.0:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")