a = input()

upper, lower = '', ''

for i in a:
    if i == i.upper():
        upper += i
    else:
        lower += i

print(a.upper() if len(upper) > len(lower) else a.lower())