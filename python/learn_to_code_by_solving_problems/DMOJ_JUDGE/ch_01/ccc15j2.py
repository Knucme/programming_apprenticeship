line = input()
H = ':-)'
S = ':-('
total_h = line.count(H)
total_s = line.count(S)

if total_h > total_s:
        print('happy')
elif total_h < total_s:
        print('sad')
elif total_h == 0 and total_s == 0:
        print('none')
else:
        print('unsure')
