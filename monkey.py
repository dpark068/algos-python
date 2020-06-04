from fractions import Fraction

def numerator(num):
    frac = Fraction(num)
    return frac.numerator

print(numerator(0.75))
