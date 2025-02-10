horseshoes = list(map(int, input().split()))

different_color = set(horseshoes)

print(len(horseshoes) - len(different_color))