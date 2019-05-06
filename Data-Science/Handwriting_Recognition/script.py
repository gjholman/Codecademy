import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()

# Use KMeans model to predict output integer
my_model = KMeans(n_clusters=10, random_state=50)
my_model.fit(digits.data)

figure = plt.figure(figsize=(8, 3))
figure.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

# Visualize center clusters
for i in range(10):
  # Initialize subplots in a grid of 2x5
  ax = figure.add_subplot(2, 5, 1+i)
  #Display
  ax.imshow(my_model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
  
plt.show()

