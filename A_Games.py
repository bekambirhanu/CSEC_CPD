n = int(input())

home, guest = [], []

count = 0

for i in range(n):
    a = list(map(int, input().split()))
    
    home.append(a[0])
    guest.append(a[1])

for i in home:
    count += guest.count(i)

print(count)