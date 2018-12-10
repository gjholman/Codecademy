import numpy as np

temperatures = np.genfromtxt('temperature_data.csv', delimiter = ',')

temperatures_fixed = temperatures + 3
print(temperatures_fixed)

# array[verticalbound, horizontalbound]
monday_temperatures = temperatures_fixed[0, 0:]
print(monday_temperatures)

thursday_friday_morning  = temperatures_fixed[3:5, 1]
print(thursday_friday_morning)

# Don't forget these gosh darn parentheses. also use bitwise symbols
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
print(temperature_extremes)
