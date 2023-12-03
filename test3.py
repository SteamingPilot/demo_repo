from sympy.parsing.latex import parse_latex
from sympy import *
import sympy

# Testing Expressions
# Test 1
# 2*3 = 6
exp1 = parse_latex("2*3")
exp2 = parse_latex("6")
print(exp1.equals(exp2))

# Test 2a - Constants
# a*b = ba
exp1 = parse_latex("a*b")
exp2 = parse_latex("ba")
print(exp1.equals(exp2))

# Test 2b
# ab = ba
exp1 = parse_latex("ab")
exp2 = parse_latex("ba")
print(exp1.equals(exp2))

# Test 2c
# 2ab = 2ba
exp1 = parse_latex("2ab")
exp2 = parse_latex("2ba")
print(exp1.equals(exp2))

# Constants 3
# (-b)/2a = (-b)/a2
exp1 = parse_latex("\\frac{-b}{2a}")
exp2 = parse_latex("\\frac{-b}{a2}")
print(exp1.equals(exp2))

# Test 4
# Sqrt and power of: sqrt(x^2 + y^2) = (x^2 + y^2)^0.5
exp1 = parse_latex("\\sqrt{5^2}")
exp2 = parse_latex("(5^2)^0.5")
print(exp1.equals(exp2))

# Test 5
# Product: prod(i, (i, 1, n)) = n!
exp1 = parse_latex("\\prod_{i=1}^{5} i")
exp2 = parse_latex("5!")
print(exp1.equals(exp2))

# Test 6
# Log: log(x^2) = 2*log(x)
# NOTE: these functions will not evaluate to TRUE when we just place "x" in
# x = symbols('x')
exp1 = parse_latex("\\log(6^2)")
exp2 = parse_latex("2\\log(6)")
print(exp1.equals(exp2))

x = symbols("x")
print("Log: ")
exp1 = parse_latex("\\log\\left(x^2\\right)")
exp2 = parse_latex("2\\log\\left(x\\right)")
print(simplify(exp1-exp2)==0)


# Test 7
# Summation: sum(i, (i, 1, n)) = n*(n+1)/2
exp1 = parse_latex("\\sum_{i=1}^{6} i")
exp2 = parse_latex("\\frac{6(6+1)}{2}")
print(exp1.equals(exp2))

# Test 8
# Sin and Cos: sin(2x) = 2*sin(x)*cos(x)
exp1 = parse_latex("\\sin(2x)")
exp2 = parse_latex("2\\sin(x)\\cos(x)")
print(exp1.equals(exp2))

# Test 9
# Distributive prop: (a+b)c = ac + bc
exp1 = parse_latex("(a+b)c")
exp2 = parse_latex("ac+bc")
print(exp1.equals(exp2))

# Test 10
# Cube: y^3 = y*y*y
exp1 = parse_latex("y^3")
exp2 = parse_latex("yyy")
print(exp1.equals(exp2))



from sympy.abc import x,y
vers1 = (x+y)**2
vers2 = x**2 + 2*x*y + y**2

# x = sympy.Symbol("x", real=True)
vers1 = log(x**2)
vers2 = 2*log(x)
vers3 = vers1.expand(force=True)
vers4 = vers2.expand(force=True)
print(simplify(vers1-vers2) == 0)
print("test: ", simplify(vers3-vers4) == 0)