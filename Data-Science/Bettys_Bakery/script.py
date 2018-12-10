import numpy as np

# Save all of the recipes from the csv file into a numpy array
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

# Make an array of the total number of eggs from each recipe
eggs = recipes[:,3]
print(eggs)

# Make a new array of True or False values based on whether or not there is 1 egg in the recipe
# using the array eggs
one_egg = np.array([egg == 1 for egg in eggs])
print(one_egg)

# Extract cookies row into its own 1-D array
cookies = recipes[2]
print(cookies)

# Extract cupcakes and double ingredients - since we are double the recipe
double_batch = recipes[0] * 2
print(double_batch)

# Create the grocery list. We are making cookies and cupcakes (which we're doubling)
grocery_list = double_batch + cookies
print(grocery_list)
