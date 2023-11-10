import matplotlib.pyplot as plt
import numpy as np

points = np.array([[0,0],[2,2],[2,-2],[-2,2],[-2,-2]])
# plot the points

# plot axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.scatter(points[:, 0], points[:, 1])
plt.show()