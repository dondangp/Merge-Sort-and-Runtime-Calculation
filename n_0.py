import matplotlib.pyplot as plt
import numpy as np

# Sample data points (n-values and times)
n_values = [1, 10, 50, 100, 500, 1000, 2000]
times = [0.000001, 0.0001, 0.0003, 0.001, 0.02, 0.05, 0.14]

# Polynomial fit (quadratic fit)
coefficients = np.polyfit(n_values, times, 2)
fitted_times = np.polyval(coefficients, n_values)

# Plotting
plt.plot(n_values, times, 'o', label="Measured Times")
plt.plot(n_values, fitted_times, '--', label="Fitted Quadratic Curve")

# Annotating n_0 without LaTeX formatting
plt.axvline(x=100, color='Purple', linestyle='--', label='n_0 ~ 100')  # Approximate n_0 without LaTeX

# Adding labels, title, and grid
plt.xlabel('n (Input Size)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of f(n) - Zoomed In')
plt.legend()
plt.grid(True)

# Zooming into the region around n_0
plt.xlim([0, 500])
plt.ylim([0, 0.03])

# Display the plot
plt.show()
