import  cv2
import numpy as np

file_pic =  '.png'

pic = cv2.imread(filename=file_pic,flags=0)
height , width  = pic.shape
mask_make  = np.zeros(shape=pic.shape)
