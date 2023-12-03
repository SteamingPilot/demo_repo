from fractions import Fraction
from decimal import Decimal


x = Fraction(0.5)
print(str(x))


# 0.56985658
# 0.569857

print(round(0.56985658, 6))




x = Fraction("0.5698565813")
y = Fraction("0.56985658")
print(x == y)

print(Fraction(Decimal("0.8857097")))






# https://stackoverflow.com/questions/23344185/how-to-convert-a-decimal-number-into-fraction
def float_to_ratio(flt):
    if int(flt) == flt:        # to prevent 3.0 -> 30/10
        return int(flt), 1
    flt_str = str(flt)
    flt_split = flt_str.split('.')
    numerator = int(''.join(flt_split))
    denominator = 10 ** len(flt_split[1])
    return numerator, denominator

# https://stackoverflow.com/questions/37112738/sympy-comparing-expressions



# 0.499999 == 0.5
print(round(0.499999, 5) == round(0.5, 5))

print(round(499999/1000000, 5) == round(0.5, 5))

print(Fraction("0.499999") == Fraction(0.5))



# 0.5 => 1/2, 0.499999 => 499999/1000000

# a^0.5 = a^(1/2) = (1/(a^(1/2))^-1)

#(0.5)^2 + (b)^2 + (c)^2  = (1/2)^2 + .....






