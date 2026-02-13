import sympy as sp

x = sp.symbols('x')
f = x**3 + 2*x**2

derivative = sp.diff(f, x)
integral = sp.integrate(f, x)
value_at_2 = derivative.subs(x, 2)

print(f)
print(derivative)
print(integral)
print(value_at_2)
