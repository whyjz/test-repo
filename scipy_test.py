#### This sample code was auto-generated using Bing's ChatGPT AI (GPT-4).

import numpy as np
from scipy import optimize

# Define the function that we want to fit
def test_func(x, a, b):
    return a * np.sin(b * x)

# Generate some data with noise to fit
x_data = np.linspace(0, 4 * np.pi, 100)
y_data = 3.0 * np.sin(1.5 * x_data) + 0.5 * np.random.normal(size=100)

# Fit the data with the function
params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2])

# Print the results
print(params)