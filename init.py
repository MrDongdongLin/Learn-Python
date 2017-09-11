import random
import math
import numpy as np
# import chaoticMap as cm

# Blocking for size 256x256
bsize = np.array([[(8, 8), (8, 16), (8, 32)],
	                [(16,8), (16,16), (16,32)],
	                [(32,8), (32,16), (32,32)]])

def BlockIndex(xw1, xw2):
	return int(math.floor(xw1*math.pow(10,14))%3), int(math.floor(xw2*math.pow(10,14))%3)

# TODD
def LargestLyapunovExponent(n=0):
	lambda_ = np.array([-0.05281413777783, -0.01751099064177, -0.02968008559044, 0.00461212897750])
	return lambda_[n]
	# return random.sample(lambda_, 1)[0]

def InitialCondition():
	lambda_ = LargestLyapunovExponent()
	x0 = abs(lambda_)
	y0 = abs(lambda_)*math.pow(10, 5) - math.floor(abs(lambda_)*math.pow(10, 5))
	x0_ = abs(lambda_)*math.pow(10, 8) - math.floor(abs(lambda_)*math.pow(10, 8))
	return x0, y0, x0_

def LogisticMap(x0, mu):
	return mu*x0*(1-x0)

def ArnoldMap_x(a, b, x0, y0):
	return (x0+a*y0)%1

def ArnoldMap_y(a, b, x0, y0):
	return (b*x0+(1+a*b)*y0)%1

def KeyGen(a, b, mu, x0, y0, x0_, n):
	sx, sy, sx_ = [], [], []
	sx.append(ArnoldMap_x(a, b, x0, y0))
	sy.append(ArnoldMap_y(a, b, x0, y0))
	sx_.append(LogisticMap(x0, mu))

	for i in range(1, n):
		sx.append(ArnoldMap_x(a, b, sx[i-1], sy[i-1]))
		sy.append(ArnoldMap_y(a, b, sx[i-1], sy[i-1]))
		sx_.append(LogisticMap(sx_[i-1], mu))

	return sx, sy, sx_
