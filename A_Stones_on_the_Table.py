n = int(input())

string = input()

left, right = 0, 1

count = 0

for i in range(n -1):
    if string[left] == string[right]:
        count += 1
    left += 1
    right += 1


print(count)
