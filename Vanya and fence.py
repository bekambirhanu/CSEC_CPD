n, h = list(map(int, input().split()))

a = list(map(int, input().split()))


count = 0
for person in a:
    if person <= h:
        count += 1
    else:
        count += 2
        
print(count)