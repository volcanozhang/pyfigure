import numpy as np
import scipy as sp
from scipy.stats import linregress
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

k, b = 1, -30
m = 200
t = np.arange(0, m, m/10)
s = k * t + b
fig, ax = plt.subplots(1)
ax.plot(t, s, 'r')
ax.annotate("",xy=(10,0),xycoords='data',xytext=(10,b),textcoords='data',arrowprops=dict(arrowstyle="<->",patchA=None,shrinkA=0,patchB=None,shrinkB=0))#,connectionstyle="arc3"),)
ax.plot((0,20),(b,b),'k')
ax.plot((0,20),(0,0),'k')
ax.text(10,b/2,'$\sigma^2-\\alpha\mu$',size='x-large')
fig.savefig('double_arrow.pdf',format='pdf', bbox_inches='tight', pad_inches=0)
