try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

except ValueError:
    print("You cannot Add strings")

else:
    print(num1 + num2)
