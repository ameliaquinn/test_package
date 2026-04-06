import numpy as np

x_arr = np.zeros(365)
y_arr = np.zeros(365)
x_sun = 0
y_sun = 0
G = 6.67e-11
M = 2e30
m = 6e24
R = 1.5e11
timestep=3600*24

def orbits(x, y, vx, vy):

    for i in range(365):

        x_arr[i] = x
        y_arr[i] = y
    
        dx = x - x_sun
        dy = y - y_sun

        dist = np.sqrt(dx**2 + dy**2)

        F = -G*M*m/(dist**2)
        Fx = F * dx/dist
        Fy = F * dy/dist

        vx += (Fx/m) * timestep
        vy += (Fy/m) * timestep

        x += vx * timestep
        y += vy * timestep

    return x_arr, y_arr