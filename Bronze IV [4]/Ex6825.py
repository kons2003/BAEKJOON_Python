# Body Mass Index
kg = float(input())
m = float(input())
bmi = kg/(m*m)

if bmi >25.0:
    print("Overweight")
elif 18.5<=bmi and bmi<=25.0:
    print("Normal weight")
else:
    print("Underweight")