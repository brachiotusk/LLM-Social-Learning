# Node Check V1

import numpy as np
from scipy.misc import imshow, imsave, imread
from scipy.ndimage import filters, morphology, measurements
from skimage.draw import line

img = imread("laGK6.jpg")

r = img[:,:, 0]
g = img[:,:, 1]
b = img[:,:, 2]

mask = (r.astype(np.float)-np.maximum(g,b) ) > 20

mask2 = morphology.binary_erosion(mask)
mask2 = morphology.binary_erosion(mask2)
mask2 = morphology.binary_erosion(mask2)
mask2 = morphology.binary_erosion(mask2)

mask2 = morphology.binary_dilation(mask2)

label, numfeatures = measurements.label(mask2)

mc = measurements.center_of_mass(mask2, label, range(1,numfeatures+1) )

mask3 = np.zeros_like(mask2)

for p in mc:
    mask3[p[0], p[1]]=255




arr = range(numfeatures)

connections=[]
for i in range( numfeatures):
    arr.remove(i)
    for j in arr:
        rr,cc = line(mc[i][0], mc[i][1], mc[j][0], mc[j][1])
        mask3[rr,cc]=255
        ms = np.sum(mask[rr,cc]).astype(np.float)/len(rr)
        if ms > 0.9:
            connections.append((i,j))


print "vertices: ", mc
print "connections: ", connections
