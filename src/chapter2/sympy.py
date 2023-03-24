#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 08:26:52 2023
# Use Spyder IDE which has in-built support for sympify.
@author: tulasiram
"""

from sympy import *

# Symbolic expression using sympify 
f = sympify("x ** 2 * sin(x)")

print(f)

# Using sympify
x = sympify("x")

f2 = sympify(x * x ** 2)
f3 = sympify(x ** 2 * sin(x))

plot(f2)
print(f2)
print(f3)

# expanding the expression using expand
f4 = expand((x - 1) * (x + 1))
f5 = expand((x - 1) ** 5)

print(f4)
print(f5)

# find the solution of an expression using solve
f6 = solve(x**2 + 2 * x - 8)
f7 = solve(sin(x) - cos(x))

print(f6)
print(f7)

# To find the differentiation(dy/dx) and integration of an expression
print(diff(f3)) # Yields x2 cos(x) + 2x sin(x)
g = integrate(f3)
print(g) # yields –x2 cos(x) + 2x sin(x) + 2 cos(x)

# To substitue a value in an expression and evaluate
result = g.subs(x, 0).evalf() # result is 2.0

print(result)

# calling plot by default gives a plot with default range of x from -10 to 10. For custom range

plot(g, (x, -20, 20))    