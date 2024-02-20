import numpy as np
import matplotlib.pyplot as plt

# Define the function
def g(x):
    return (1/3) * np.sin(2 * x)

# Generate x values
x_values = np.linspace(0, 2 * np.pi, 1000)  # Generate 1000 points between 0 and 2*pi

# Calculate y values
y_values = g(x_values)

# Plot the graph
plt.plot(x_values, y_values, label='$g(x) = \\frac{1}{3}\\sin(2x)$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Graph of $g(x) = \\frac{1}{3}\\sin(2x)$')
plt.grid(True)
plt.legend()
plt.show()

