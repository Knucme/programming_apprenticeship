

while True:
    age = int(input("Enter a age: "))

    if age < 0 or age > 150:
        break
    else:

        if age < 3:
            print("Free admission fee")
        elif age >= 3 and age < 12:
            print("$10 admission fee")
        elif age >= 12:
            print("$15 admission fee")

