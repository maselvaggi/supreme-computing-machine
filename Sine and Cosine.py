
#%%
import numpy as np
import matplotlib.pyplot as plt


#%%
arr = np.arange(0,2*np.pi, 0.1)

x = np.sin(arr)
y = np.cos(arr)

#plot and show the sine & cosine graph with legend and title
plt.plot(arr, x, label = "sine")
plt.plot(arr, y, label = "cosine")
plt.title("Sine and Cosine Graphs", fontsize = 20)
plt.legend(loc = 'lower left')
plt.show


