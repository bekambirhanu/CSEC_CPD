n = int(input())

event = list(map(int, input().split()))

police = 0

crime = 0
for i in event:
    if i != -1:
        police += i
    else:
        if police >0:
            police -= 1
        else:
            crime += 1

print(crime)


