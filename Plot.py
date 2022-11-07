import matplotlib.pyplot as plt
import numpy as np
from objFinder import *

for eachObject in detections:
    x = np.array(eachObject["name"])
y = np.array([3, 8, 2])

plt.bar(x,y,color="green")
plt.show()