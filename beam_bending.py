#import numpy as np
#import scipy as sp
#from scipy.stats import linregress
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import matplotlib.patches as patches

left, width = .1, .8
bottom, height = .1, .2

fig = plt.figure()
ax = fig.add_axes([0,0,1,2.5])
p = patches.Rectangle((left, bottom), width, height,fill=False, transform=ax.transAxes, clip_on=False)
ax.add_patch(p)
#ax.plot([0,0.18],[0.3,0.1])#,'.')
ax.annotate("",xy=(0.5,0.1),xycoords='data',xytext=(0.5,0),textcoords='data',arrowprops=dict(arrowstyle="->",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
ax.annotate("",xy=(0.7,0.4),xycoords='data',xytext=(0.7,0.3),textcoords='data',arrowprops=dict(arrowstyle="<-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
#ax.plot((0,0.18),(0.3,0.1))
ax.annotate("",xy=(0.02,0.3),xycoords='data',xytext=(0.18,0.1),textcoords='data',arrowprops=dict(arrowstyle="-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
ax.annotate("",xy=(0.02,0.3),xycoords='data',xytext=(0.1,0.3),textcoords='data',arrowprops=dict(arrowstyle="-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
ax.annotate("",xy=(0.02+0.08/3,0.3-0.2/6),xycoords='data',xytext=(0.1,0.3-0.2/6),textcoords='data',arrowprops=dict(arrowstyle="-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
ax.annotate("",xy=(0.02+0.16/3,0.3-0.4/6),xycoords='data',xytext=(0.1,0.3-0.4/6),textcoords='data',arrowprops=dict(arrowstyle="-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
ax.annotate("",xy=(0.1+0.16/3,0.1+0.2/6),xycoords='data',xytext=(0.1,0.1+0.2/6),textcoords='data',arrowprops=dict(arrowstyle="-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))
ax.annotate("",xy=(0.1+0.08/3,0.1+0.4/6),xycoords='data',xytext=(0.1,0.1+0.4/6),textcoords='data',arrowprops=dict(arrowstyle="-",patchA=None,shrinkA=0,patchB=None,shrinkB=0))

ax.set_axis_off()
plt.show()
#fig.savefig('beam_bending.pdf',format='pdf', bbox_inches='tight', pad_inches=0)
