string = input()

instr = input()

position = 0

for i in instr:
    if i == string[position]:
        position += 1

print(position + 1)