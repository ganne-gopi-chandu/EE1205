from sympy import symbols, simplify

# Define symbolic variable s
s_L= symbols('s_L')


# Given roots
s5 = 0.1621 + 1.0033j
s6 = 0.3913 + 0.4156j
s7 = 0.3913 - 0.4156j
s8 = 0.1621 - 1.0033j

# Define the given polynomial expression
polynomial_expr = 0.3125 / ((s_L - s5) * (s_L - s6) * (s_L - s7) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
