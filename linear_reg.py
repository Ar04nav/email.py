import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([[1], [2], [3], [4], [5]])  # Hours
y = np.array([35, 45, 50, 60, 70])       # Marks

# Create model and fit
model = LinearRegression()
model.fit(X, y)

# Predict
predicted = model.predict(X)

# Print slope and intercept
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# Predict marks for 6 hours
print("Predicted marks for 6 hours:", model.predict([[6]])[0])

# Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, predicted, color='red', label='Predicted Line')
plt.xlabel('Hours Studied')
plt.ylabel('Marks')
plt.legend()
plt.title('Simple Linear Regression')
plt.show()


