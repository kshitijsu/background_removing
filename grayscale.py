import numpy as np
from PIL import Image

img = Image.open('./test_images/cropped.jpg')
array = np.array(img)

array = 255 - array

invimg = Image.fromarray(array)
invimg.save('./test_images/testgrey-inverted.png')
