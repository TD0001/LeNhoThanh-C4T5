mass = float(input("enter your mass in kilogram: "))
height = float(input("enter your height in centimeter: "))
height = height / 100
BMI = mass / (height ** 2)
print("Your BMI is ", BMI)