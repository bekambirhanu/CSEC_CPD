import fractions

a = tuple(map(int, input().split()))

dot = ((6+1) - max(a[0], a[1]))/ 6

if dot == 0 or dot == 1:
    print(f'{int(dot)}/1')
else:
    fract = fractions.Fraction(dot).limit_denominator()
    print(fract)