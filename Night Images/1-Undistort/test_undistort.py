import cv2
from scipy.misc import imsave
from undistortImg import *

image_loc = './2017-01-13-20-28-03-wahrsis3.jpg'

im = cv2.imread(image_loc)
unImage = undistortCC(im)
path_components = image_loc.split("/")
image_name = path_components[len(path_components)-1]

withoutExt = image_name.split(".")
withoutExt_name = withoutExt[0]
SaveFigFileName = withoutExt[0] + '-undist.' + withoutExt[1]
imsave('./'+SaveFigFileName, unImage[:,:,[2,1,0]])
