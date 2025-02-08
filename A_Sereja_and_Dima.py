n = int(input())

card = list(map(int, input().split()))

logic = True
sereja, dima = 0, 0

left, right = 0, len(card) - 1

while left<=right:
    
    if card[left] >= card[right]:
        if logic:
            sereja += card[left]
            logic = not logic
        else:
            dima += card[left]
            logic = not logic
        left += 1
    else:
        if logic:
            sereja += card[right]
            logic = not logic
        else:
            dima += card[right]
            logic = not logic
        right -= 1

print(sereja, dima)