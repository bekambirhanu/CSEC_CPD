a, b = map(int, input().split())

constant = a

count = 1
while a%10 != 0 and a%10 != b:
    
    a += constant
    
    count += 1

print(count)

