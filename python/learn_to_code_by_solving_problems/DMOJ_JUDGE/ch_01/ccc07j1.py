num1 = int(input())
num2 = int(input())
num3 = int(input())

largest = num1
middle = 0
small = 0

if num1 > num2 and num1 > num3:
    largest = num1
    if num2 > num3:
        middle = num2
        small = num3
    else:
        middle = num3
        small = num2

elif num2 > num1 and num2 > num3:
    largest = num2
    if num1 > num3:
        middle = num1
        small = num3
    else:
        middle = num3
        small = num1
elif num3 > num2 and num3 > num1:
    largest = num3
    if num2 > num1:
        middle = num2
        small = num1
    else:
        middle = num1
        small = num2

print(middle)
