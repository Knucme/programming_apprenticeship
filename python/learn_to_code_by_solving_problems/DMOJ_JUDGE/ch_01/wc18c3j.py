P = int(input())
B = int(input())
D = int(input())

R = ((P//B) * D) + ((P - ((P//B) * B)) * 1)

print(R)
