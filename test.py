# Configuring the sympy was a bit tricky
# It needed a very specific version of antlr4 package, at a very specific location
from sympy.parsing.latex import parse_latex

# used for evaluating functions with "x" and "y"
# note: not working at the moment
from sympy import symbols
from sympy import var
from sympy.abc import X,Y


import sympy as sp
import numpy as np
def check_equal(Expr1, Expr2, n=10, positive=False, strictly_positive=False):
    
    # Determine over what range to generate random numbers
    sample_min = -1
    sample_max = 1
    if positive:
        sample_min = 0
        sample_max = 1
    if strictly_positive:
        sample_min = 1
        sample_max = 2
    
    # Regroup all free symbols from both expressions
    free_symbols = set(Expr1.free_symbols) | set(Expr2.free_symbols)
    
    # Numeric (brute force) equality testing n-times
    for i in range(n):
        your_values=np.random.uniform(sample_min, sample_max, len(free_symbols))
        Expr1_num=Expr1
        Expr2_num=Expr2
        for symbol,number in zip(free_symbols, your_values):
            Expr1_num=Expr1_num.subs(symbol, sp.Float(number))
            Expr2_num=Expr2_num.subs(symbol, sp.Float(number))
        Expr1_num=float(Expr2_num)
        Expr2_num=float(Expr2_num)
        if not np.allclose(Expr1_num, Expr2_num):
            print("Fails numerical test")
            return(False)
        
    # If all goes well so far, check symbolic equality
    if (Expr1.equals(Expr2)):
        return(True)

    else:
        print("Passes the numerical test but not the symbolic test")
        # Still returns true though
        return(True)





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
x = symbols('x')
exp1 = parse_latex("\\log(6^2)")
exp2 = parse_latex("2\\log(6)")
print(exp1.equals(exp2))

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


var("x y")
# Test 11
exp1 = parse_latex("\\sqrt{X^2+Y^2}")
exp2 = parse_latex("\\left(X^2+Y^2\\right)^{0.5}")
print(exp1.equals(exp2))



# Test 12
exp1 = parse_latex("x^{0.5}")
exp2 = parse_latex("x^{\\frac12}")
print(exp1.equals(exp2))


# Test 13
exp1 = parse_latex("{\\frac12}")
exp2 = parse_latex("{\\frac{499999}{1000000}}")
print(exp1.equals(exp2))

exp1 = parse_latex("xy")
exp2 = parse_latex("yx")
print(exp1.equals(exp2))

exp1 = parse_latex("\\sqrt{X^2+Y^2}")
exp2 = parse_latex("\\left(X^2+Y^2\\right)^{0.5}")
print(exp1.evalf() == exp2.evalf())

exp1 = parse_latex("\\left(X^2+Y^2\\right)^{0.49999}")
exp2 = parse_latex("\\left(X^2+Y^2\\right)^{0.5}")
print(exp1.evalf() == exp2.evalf())


exp1 = parse_latex("\\left(X^2+Y^2\\right)^{0.49999}")
exp2 = parse_latex("\\left(X^2+Y^2\\right)^{0.5}")
print(exp1.evalf(4) == exp2.evalf(4))


expr = 2*x
print(expr.evalf(3,subs={x: 0.0010001}))
print(expr.evalf(3,subs={x: 0.0010001}, chop=True))



