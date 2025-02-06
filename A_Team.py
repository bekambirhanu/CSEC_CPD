n = int(input())

count = 0

for i in range(n):
    poll = input()

    if poll.count('1') >= 2:
        count += 1

print(count)