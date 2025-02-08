cal = list(map(int, input().split()))

s = list(map(int, input()))

count = 0

for i in s:
    
    index = i-1
    
    count += cal[index]
    
print(count)