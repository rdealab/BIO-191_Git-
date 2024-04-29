num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter another integer: "))
num3 = int(input("Please enter a third integer: "))

largest= None

if num1 % 2 != 0:
    largest= num1

if num2 % 2 != 0 and (largest is None or num2 > largest):
    largest = num2

if num3 % 2 != 0 and (largest is None or num3 > largest):
    largest = num3

if largest is not None:
    print(largest, "is the greatest odd integer.")
else:
    print("None of the integers are odd.")