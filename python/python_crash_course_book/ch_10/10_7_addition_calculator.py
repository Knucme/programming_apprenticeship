usr_cont = ''

while True:
    if usr_cont == 'q':
        break
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))

    except ValueError:
        print("You cannot Add strings")

    else:
        print(num1 + num2)
    usr_cont = input("press q to quit!\nPress Enter to Continue: ")
