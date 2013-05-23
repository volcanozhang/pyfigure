import numpy as np
from matplotlib.patches import ConnectionPatch
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
gs = gridspec.GridSpec(10, 10)

plt.plot([0,0,1],[0,1,1],'k')
plt.plot([0,1,1],[0,0,1],'k')
plt.axis('off')

nx, ny = 4, 4
dx, dy = 1./(nx+1), 1./(ny+1)
for i in range(1,nx+1):
    for j in range(1,ny+1):
        plt.plot([dx*i,dx*i],[0,1],'k')
        plt.plot([0,1],[dy*j,dy*j],'k')
plt.text(0.5, 0.5, "$(i,j)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5-dx, 0.5-dy, "$(i-1,j-1)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5-dx, 0.5, "$(i-1,j)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5-dx, 0.5+dy, "$(i-1,j+1)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5, 0.5+dy, "$(i,j+1)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5, 0.5-dy, "$(i,j-1)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5+dx, 0.5+dy, "$(i+1,j+1)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5+dx, 0.5, "$(i+1,j)$", horizontalalignment='center',verticalalignment='center', size='x-large')
plt.text(0.5+dx, 0.5-dy, "$(i+1,j-1)$", horizontalalignment='center',verticalalignment='center', size='x-large')
#plt.show()
plt.savefig('pixel_ij.pdf',format='pdf', bbox_inches='tight', pad_inches=0)
