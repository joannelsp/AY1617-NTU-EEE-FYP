import numpy as np
import cv2
from PIL import Image

data = np.load('wahrsis3-PZA.npy')
rescale = (255.0/(np.nanmax(data) - np.nanmin(data)) * (data - np.nanmin(data))).astype('uint8')
img = Image.fromarray(rescale)
img.save('PZA.png')
