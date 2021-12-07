import math
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = float(weight / math.pow(height, 2))

if bmi < 18.5:
    print(f"you bmi is: {bmi:.1f} you're underweight")
elif 18.5 <= bmi < 25:
    print(f"you bmi is: {bmi:.1f} your weight is normal")
elif 25 <= bmi < 30:
    print(f"you bmi is: {bmi:.1f} you're overweight")
elif 30 <= bmi < 35:
    print(f"you bmi is: {bmi:.1f} you're obese")
else:
    print(f"you bmi is: {bmi:.1f}You're clinically obese")
