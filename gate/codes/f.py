import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 3 * np.cos(2 * x)

# Generate x values
x_values = np.linspace(0, 2 * np.pi, 1000)  # Generate 1000 points between 0 and 2*pi

# Calculate y values
y_values = f(x_values)

# Plot the graph
plt.plot(x_values, y_values, label='$f(x) = 3\cos(2x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of $f(x) = 3\cos(2x)$')
plt.grid(True)
plt.legend()
plt.show()

