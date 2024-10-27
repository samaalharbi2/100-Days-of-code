weight = 85
height = 1.85

bmi = weight / (height ** 2)

bmi = float(input("Enter your bmi?"))

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi <25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("overweight")
else:
    print("Obesity")