n = int(input())
s = input()

count_A = s.count('A') 
count_D = n - count_A

if count_A > count_D:
    print('Anton')
elif count_A < count_D:
    print('Danik')
else:
    print('Friendship')
