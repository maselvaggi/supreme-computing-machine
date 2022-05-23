#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
arr = np.arange(0,2*np.pi, 0.1)

x = np.sin(arr)
y = np.cos(arr)

#plot and show the sine/cosine graphs
plt.plot(arr, x)
plt.plot(arr, y)
plt.show


# %%
