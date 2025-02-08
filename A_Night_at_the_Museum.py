word = input()

letters = [chr(i) for i in range(97, 123)]

count = 0

last_letter = 'a'

for i in word:
    
    anticlock =abs(letters.index(last_letter) - letters.index(i))
    
    if anticlock <= 13:
        count += anticlock
    
    else:
        count += 26 - anticlock
    
    last_letter = i

print(count)