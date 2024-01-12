import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Data points
x = np.array([-0.015, -0.01, -0.005, 0.0, 0.005, 0.01, 0.015])
y = np.array([0.063, 0.025, 0.004, 0.0, 0.017, 0.046, 0.093])

# Fit a polynomial curve of degree 2
degree = 2
coefficients = np.polyfit(x, y, degree)
curve_fit = np.poly1d(coefficients)

# Generate x values for the curve
x_curve = np.linspace(min(x), max(x), 100)
y_curve = curve_fit(x_curve)

# Calculate the second derivative of the curve
second_derivative = np.polyder(curve_fit, m=2)

# Calculate the root mean squared error (RMSE)
y_predicted = curve_fit(x)
rmse = np.sqrt(mean_squared_error(y, y_predicted))

# Save data points to .dat file
data_points = np.column_stack((x, y))
np.savetxt('data_points.dat', data_points, delimiter=' ', header='x y', comments='')

# Save fitting data points to .dat file
fitting_points = np.column_stack((x_curve, y_curve))
np.savetxt('fitting_points.dat', fitting_points, delimiter=' ', header='x y', comments='')

# Plot the data points and curve fit
plt.scatter(x, y, label='Data Points')
plt.plot(x_curve, y_curve, color='red', label='Curve Fit (degree = 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting')
plt.legend()
plt.show()

print(f"Root Mean Squared Error (RMSE): {rmse}")
print("Data points saved to 'data_points.dat'")
print("Fitting data points saved to 'fitting_points.dat'")

# Calculate the second derivative at a specific x value
x_value = 0.0
second_derivative_value = second_derivative(x_value)
print(f"Second derivative at x = {x_value}: {second_derivative_value}")
