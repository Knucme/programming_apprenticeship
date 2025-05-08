M = int(input())
D = int(input())
O = ''

if M == 1:
    O = 'Before'

elif M == 2:
    if D > 18:
        O = 'After'
    elif D < 18:
        O = 'Before'

    else:
        O = 'Special'
else:
    O = 'After'

print(O)
