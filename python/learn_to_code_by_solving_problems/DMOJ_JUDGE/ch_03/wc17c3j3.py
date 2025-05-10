password = input()
lowercase_letter = 0
upercase_letter = 0
digit = 0

if len(password) <= 12 and len(password) >= 8:
        for char in password:
            if char.isdigit() == True:
                digit += 1
            elif char == char.lower():
                lowercase_letter += 1
            elif char == char.upper():
                upercase_letter += 1
        if lowercase_letter >= 3 and upercase_letter >= 2 and digit >= 1:
            print('Valid')
        else:
            print('Invalid')
else:
    print('Invalid')
