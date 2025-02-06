n = input()

h = input()

a = input().split()
result = 0
for i in a:
    if int(i) > int(h):
        result += 2
    else:
        result += 1
print(result)

