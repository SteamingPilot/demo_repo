from sympy.parsing.latex import parse_latex
from sympy import *
import sympy



exp1 = parse_latex("\\sqrt{x+y}")
exp2 = parse_latex("(x+y)^0.5")
exp3 = parse_latex("\\left(x+y\\right)^{\\frac12}")

print(exp1.equals(exp2))
print(exp1.equals(exp3))

print(exp1.evalf(2) == exp2.evalf(2))
print(exp1.evalf(2) == exp3.evalf(2))




