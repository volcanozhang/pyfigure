import numpy as np
from matplotlib.patches import ConnectionPatch
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.image as mpimg
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
gs = gridspec.GridSpec(2, 3)
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[1, 0])
ax = plt.subplot(gs[:, 1:3])

xy1 = (1390, 1186)
xy2 = (473, 1408)
image = np.load('image.npy')
ax.imshow(np.log(image), interpolation="none", aspect="auto", cmap=cm.Greys_r)
subimage1 = image[xy1[1]-10:xy1[1]+10,xy1[0]-10:xy1[0]+10]
subimage2 = image[xy2[1]-10:xy2[1]+10,xy2[0]-10:xy2[0]+10]
ax1.imshow(np.log(subimage1), interpolation="none", aspect="auto", cmap=cm.Greys_r)
ax2.imshow(np.log(subimage2), interpolation="none", aspect="auto", cmap=cm.Greys_r)

xy = (11, 11)

con1 = ConnectionPatch(xyA=xy, xyB=xy1, coordsA="data", coordsB="data",
                       axesA=ax1, axesB=ax,
                       arrowstyle="->", shrinkB=5, color='r')
con2 = ConnectionPatch(xyA=xy, xyB=xy2, coordsA="data", coordsB="data",
                       axesA=ax2, axesB=ax,
                       arrowstyle="->", shrinkB=5, color='r')
ax.add_artist(con1)
ax1.add_artist(con1)
ax.add_artist(con2)
ax2.add_artist(con2)

#rect = patches.Rectangle((5, 5), 11, 11, fill=False, ls='solid')
#ax1.add_patch(rect)
ax1.plot([5,5,16,16,5], [5,16,16,5,5])
#ax1.axis([0,20,0,20])
#ax1.axes.get_xaxis().set_visible(False)
#ax1.axes.get_yaxis().set_visible(False)
ax1.axis('off')
ax2.plot([5,5,16,16,5], [5,16,16,5,5])
#ax2.axis([0,20,0,20])
#ax2.axes.get_xaxis().set_visible(False)
#ax2.axes.get_yaxis().set_visible(False)
ax2.axis('off')

ax.axis('off')
#plt.show()
plt.savefig('spot.pdf',format='pdf', bbox_inches='tight', pad_inches=0)
