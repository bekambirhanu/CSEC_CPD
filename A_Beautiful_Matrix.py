Mx = []
A =list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
E = list(map(int, input().split()))

Mx.append(A)
Mx.append(B)
Mx.append(C)
Mx.append(D)
Mx.append(E)

for i in range(5):
    if 1 in Mx[i]:
        row, column = i, Mx[i].index(1)
        break


print(abs(row-2) + abs(column-2))
