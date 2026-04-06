from ..code_one_M import orbits

import numpy as np
import random

def test_orbits():
	x = 1.5e11
	y = 0
	vx = 0
	vy = np.sqrt(((6.67e-11)*(2e30))/(1.5e11))

	x_arr, y_arr = orbits(x,y,vx,vy)

	num = random.randint(1, 364)
	R_final = np.sqrt(x_arr[num]**2 + y_arr[num]**2)
	print(R_final)

	assert abs(1.5e11 - R_final) < 10e9

