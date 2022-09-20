import math
import matplotlib
import sympy

x = sympy.symbols("x")
R=sympy.symbols("R")
t=sympy.symbols("t")
a=sympy.solve([sympy.tan(x)-t/1.12,R**2-(R-t)**2-1.12**2,R*x-1.31],[x,R,t])
print(a)