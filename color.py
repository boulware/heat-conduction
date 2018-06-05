import numpy as np
import colorsys
from skimage.color import hsv2rgb
from skimage import data

class Color:
	def __init__(self, rgb=None, hsv=None):
		if rgb:
			self.hsv = np.asarray(colorsys.rgb_to_hsv(*rgb))
		elif hsv:
			self.hsv = np.asarray(hsv)

	def __mul__(self, constant):
		return constant * self.hsv

	def __rmul__(self, constant):
		return self.__mul__(constant)


np.set_printoptions(threshold=np.nan)

# (np vectorized) Linear interpolates between two colors in HSV, where weight=0.0 => color[0] and weight=1.0 => color[1]
def InterpolateColors(color_pairs, weights):
	#print('pairs={}'.format(color_pairs))
	#print('weights={}'.format(weights))
	return hsv2rgb((1.0 - weights) * color_pairs[:,0] + (weights) * color_pairs[:,1])

if __name__=='__main__':
	img = data.astronaut()
	print(type(img))

	red = Color(rgb=(1,0,0))
	green = Color(rgb=(0,1,0))
	black = Color(rgb=(0,0,0))	
	white = Color(rgb=(1,1,1))

	colors = np.array([[green, red], [black, white]])
	weights = np.array([1.0, 0.5])

	InterpolateColors(colors, weights)