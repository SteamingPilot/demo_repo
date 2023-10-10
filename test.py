from sympy.parsing.latex import parse_latex

# Testing Expressions

# 2*3 = 6
exp1 = parse_latex("2*3")
exp2 = parse_latex("6")
print(exp1.equals(exp2))

# Constants 1
# a*b = ba
exp1 = parse_latex("a*b")
exp2 = parse_latex("ba")
print(exp1.equals(exp2))

# Constants 2
# ab = ba
exp1 = parse_latex("ab")
exp2 = parse_latex("ba")
print(exp1.equals(exp2))

# Constants 3
# 2ab = 2ba
exp1 = parse_latex("2ab")
exp2 = parse_latex("2ba")
print(exp1.equals(exp2))

# Constants 3
# (-b)/2a = (-b)/a2
exp1 = parse_latex("\\frac{-b}{2a}")
exp2 = parse_latex("\\frac{-b}{a2}")
print(exp1.equals(exp2))
 



