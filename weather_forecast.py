import numpy as np

# Step 1: Load temperature data from CSV
data = np.genfromtxt("temperatures.csv", delimiter=",", skip_header=1)
temperatures = data[:, 1]  # column 1 is temperature

print("Temperature Data:", temperatures)

# Step 2: Basic Weather Analysis
average_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

print("\nWeather Statistics:")
print("Average Temperature:", average_temp)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

# Step 3: Weather Forecast (Moving Average)
last_n_days = 5
forecast_temp = np.mean(temperatures[-last_n_days:])

print("\nWeather Forecast:")
print("Predicted Temperature for Next Day:", round(forecast_temp, 4), "°C")
