import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#Calculate the total count of responses saying ceballos
total_ceballos = sum([1 for n in survey_responses if n == "Ceballos"])
print(total_ceballos)

#Calculate the percentage of votes for ceballos
survey_length = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos / survey_length
print(percentage_ceballos)

#Create binomial distribution centered around 54% of the votes
# N = Survey Length
# P = 0.54
# size = total population size
possible_surveys = np.random.binomial(survey_length, 0.54, size = 10000)
possible_surveys_percent = possible_surveys / survey_length
print(possible_surveys_percent)

# Create a histogram plot for this binomial distribution with 20 bins
plt.hist(possible_surveys_percent, bins=20, range=(0,1))
#plt.show()

#Find the percent chance of Ceballos losing
# Ans. = 21.2 %
ceballos_loss_surveys = np.mean(possible_surveys_percent < 0.5)
print(ceballos_loss_surveys)

# Create a new binomial distributon with 7000 people
# N = 7000
# P = 0.54
# Size = 10000
large_survey = np.random.binomial(7000., 0.54, size = 10000) / 7000.
print(large_survey)

# Add new data to histogram plot
plt.hist(large_survey, range=(0,1), bins=20, alpha=0.5) # Alpha = opacity
plt.show()

# Find new percent of Ceballos losing
# Ans. = 0.00 %
ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)
