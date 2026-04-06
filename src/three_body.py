import numpy as np

masses = [1,1,1]
G = 1
num_points = 10000
dt = 0.001

def three_body(x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3):
    x_arr = [np.zeros(num_points + 1), np.zeros(num_points + 1), np.zeros(num_points + 1)]
    x_arr[0][0] = x1
    x_arr[1][0] = x2
    x_arr[2][0] = x3
    y_arr = [np.zeros(num_points + 1), np.zeros(num_points + 1), np.zeros(num_points + 1)]
    y_arr[0][0] = y1
    y_arr[1][0] = y2
    y_arr[2][0] = y3
    vx_arr = [np.zeros(num_points + 1), np.zeros(num_points + 1), np.zeros(num_points + 1)]
    vx_arr[0][0] = vx1
    vx_arr[1][0] = vx2
    vx_arr[2][0] = vx3
    vy_arr = [np.zeros(num_points + 1), np.zeros(num_points + 1), np.zeros(num_points + 1)]
    vy_arr[0][0] = vy1
    vy_arr[1][0] = vy2
    vy_arr[2][0] = vy3
    

    for i in range(num_points):
        for j in range(len(masses)):
            Fx = 0
            Fy = 0
            for k in range(len(masses)):
                if (j == k):
                    continue
                else:
                    dist = np.sqrt((x_arr[j][i] - x_arr[k][i])**2 + (y_arr[j][i] - y_arr[k][i])**2)
                    F = - G * masses[j] * masses[k] / (dist ** 2)
                    Fx += F * (x_arr[j][i] - x_arr[k][i]) / dist
                    Fy += F * (y_arr[j][i] - y_arr[k][i]) / dist
            ax = Fx / masses[j]
            ay = Fy / masses[j]
            vx = vx_arr[j][i] + (ax * dt)
            vy = vy_arr[j][i] + (ay * dt)
            x = x_arr[j][i] + (vx * dt)
            y = y_arr[j][i] + (vy * dt)
            x_arr[j][i+1] = x
            y_arr[j][i+1] = y
            vx_arr[j][i+1] = vx
            vy_arr[j][i+1] = vy
    return x_arr, y_arr