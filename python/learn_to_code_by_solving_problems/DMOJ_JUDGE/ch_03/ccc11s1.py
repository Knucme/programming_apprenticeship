N = int(input())
t_count = 0
s_count = 0

for i in range(N):
    S = input()
    for letter in S:
        if letter.lower() == 't':
            t_count += 1
        elif letter.lower() == 's':
            s_count += 1

if t_count > s_count:
    print("English")
else:
    print("French")
