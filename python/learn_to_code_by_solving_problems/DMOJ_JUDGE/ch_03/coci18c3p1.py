N = input()
count = 0
word = ''

for i in N:
    if i == 'H' and 'O' not in word and 'N' not in word and 'I' not in word and 'H' not in word:
        word += i
    elif i == 'O' and 'N' not in word and 'I' not in word and 'O' not in word and 'H' in word:
        word += i
    elif i == 'N' and 'I' not in word and 'N' not in word and 'H' in word and 'O' in word:
        word += i
    elif i == 'I' and 'I' not in word and 'H' in word and 'O' in word and 'N' in word:
        word += i
    if word == 'HONI':
        count += 1
        word = ''

print(count)

