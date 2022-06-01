
#%%
from cmath import sin
import numpy as np
import matplotlib.pyplot as plt


#%%
# x - start of range
# y - end of range
# z - frequency of points plotted
def sincos(x,y,z):
    arr = np.arange(x,y*np.pi, z)

    x = np.sin(arr)
    y = np.cos(arr)

    #plot and show the sine & cosine graph with legend and title
    plt.plot(arr, x, label = "sine")
    plt.plot(arr, y, label = "cosine")
    plt.title("Sine and Cosine Graphs", fontsize = 20)
    plt.legend(loc = 'lower left')
    plt.show

# %%
if __name__ == "__main__":
    #sincos(0,2,0.1)
    #sincos(10,5,0.5)
    sincos(-5,3,1)       
