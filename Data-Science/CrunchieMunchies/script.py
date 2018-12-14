# This project uses numpy to help a food company's new cereal: CrunchieMunchies
import codecademylib
import numpy as np

# cereal.csv contains a list of cereal's calories
calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
# print(calorie_stats)

# calories in crunchie munchies
crunchie_munchie_cal = 60
average_calories = np.mean(calorie_stats)

print('CrunchieMunchie Calories: \t{0}\nOther Cereal Average: \t\t{1}'.format(crunchie_munchie_cal, average_calories))

calorie_stats_sorted = np.sort(calorie_stats) 
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print('Other Cereal Median Calories: \t{0}'.format(median_calories))

# Find the nth percentile where the calories count is less than 60
nth_percentile = np.percentile(calorie_stats, 3)
print(nth_percentile)

#Percentage of Cereals with calories greater than 60
# np.mean on a filtered array in the function call outputs the percentage of that statistic
more_calories = np.mean(calorie_stats > 60)
print(more_calories)

calorie_std = np.std(calorie_stats)
print(calorie_std)

"""
This shows that CrunchieMunchie is in the top 4% of cereals in terms of calorie count. Perhaps marketing can use this statistic to the company's advantage
"""
