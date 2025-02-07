s = 0
count = 0

n = int(input())

for i in range(n):
    a = int(input())
    
    if a != s:
        count += 1
        s = a
print(count)