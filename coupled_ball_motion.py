"""
Author: Kemal Rizky F 10219113
"""

import math
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

# Initial velocity
vx1, vy1 = [0.0], [0.0]
vx2, vy2 = [0.0], [0,0]

# Instantaneous velocity when the particle hit the ground
vy1_ground, vy2_ground = 0.0, 0.0

# Initial position
# Particle 1
x1, y1 = [3.0], [6.0]
#Particle 2
x2, y2 = [4.0], [5.0]

#Initial acceleration
ay1 = [0.0]
ay2 = [0.0]
ax1 = [0.0]
ax2 = [0.0]

# String length
l0 = math.sqrt((x1[0] - x2[0])**2 + (y1[0] - y2[0])**2)  # Initial length
l = [l0]

# Initializing time array
t = [0.0]

# Initializing other parameters
k = 11
m1 = 1
m2 = 1
g = 9.8

if x1[0]-x2[0] == 0:
    theta = math.pi/2
else:
    theta = math.atan(abs((y1[0] - y2[0])/(x1[0]-x2[0])))
# theta = math.atan(abs((y1[0] - y2[0])/(x1[0]-x2[0])))
delta_l = abs(l[0]-l[0])
delta_t = 0.001
epsilon = 0.01


i = 1

def Fs_x(angle, delta_string):
    return k * delta_string * math.cos(angle)

def Fs_y(angle, delta_string):
    return k * delta_string * math.sin(angle)

while True:       
    y1.append(0.0)
    x1.append(0.0)
    vy1.append(0.0)
    vx1.append(0.0)
    ay1.append(0.0)
    ax1.append(0.0)
    y2.append(0.0)
    x2.append(0.0)
    vy2.append(0.0)
    vx2.append(0.0)
    ay2.append(0.0)
    ax2.append(0.0)
    t.append(0.0)
    l.append(0.0)
    
    t[i] = t[i-1] + delta_t

    # Updating acceleration
    if (l[i-1] >= l[0] and l[i-1] <= l[0]*1.1):       # If string streches
        if y1[i-1] > y2[i-1]:
            if x1[i-1] < x2[i-1]:
                ay1[i] = -(Fs_y(theta, delta_l)/m1 + g)
                ax1[i] = Fs_x(theta, delta_l)/m1

                ay2[i] = Fs_y(theta, delta_l)/m2 - g 
                ax2[i] = -Fs_x(theta, delta_l)/m2
            elif x1[i-1] > x2[i-1]:
                ay1[i] = -(Fs_y(theta, delta_l)/m2 + g)
                ax1[i] = -Fs_x(theta, delta_l)/m2
                
                ay2[i] = Fs_y(theta, delta_l)/m1 - g 
                ax2[i] = Fs_x(theta, delta_l)/m1
            else:
                ay1[i] = -(Fs_y(math.pi/2, delta_l)/m2 + g)
                ax1[i] = 0.0
                
                ay2[i] = Fs_y(math.pi/2, delta_l)/m1 - g 
                ax2[i] = 0.0

        elif y1[i-1] < y2[i-1]:
            if x1[i-1] < x2[i-1]:
                ay1[i] = Fs_y(theta, delta_l)/m1 - g 
                ax1[i] = Fs_x(theta, delta_l)/m1

                ay2[i] = -(Fs_y(theta, delta_l)/m2 + g)
                ax2[i] = -Fs_x(theta, delta_l)/m2
            elif x1[i-1] > x2[i-1]:
                ay1[i] = Fs_y(theta, delta_l)/m1 - g 
                ax1[i] = -Fs_x(theta, delta_l)/m1

                ay2[i] = -(Fs_y(theta, delta_l)/m2 + g)
                ax2[i] = Fs_x(theta, delta_l)/m2
            else:
                ay1[i] = Fs_y(math.pi/2, delta_l)/m2 - g
                ax1[i] = 0.0
                
                ay2[i] = -(Fs_y(math.pi/2, delta_l)/m1 + g)
                ax2[i] = 0.0
        else:
            ay1[i] = -g
            ax1[i] = Fs_x(theta, delta_l)/m1

            ay2[i] = -g
            ax2[i] = -Fs_x(theta, delta_l)/m2
    elif (l[i-1] <= l[0] and l[i-1] >= l[0]*0.9):     # If string compresses
        if y1[i-1] > y2[i-1]:
            if x1[i-1] < x2[i-1]:
                ay1[i] = Fs_y(theta, delta_l)/m1 - g
                ax1[i] = -Fs_x(theta, delta_l)/m1

                ay2[i] = -(Fs_y(theta, delta_l)/m2 + g) 
                ax2[i] = Fs_x(theta, delta_l)/m2
            elif x1[i-1] > x2[i-1]:
                ay1[i] = Fs_y(theta, delta_l)/m1 - g
                ax1[i] = Fs_x(theta, delta_l)/m1

                ay2[i] = -(Fs_y(theta, delta_l)/m2 + g) 
                ax2[i] = -Fs_x(theta, delta_l)/m2
            else:
                ay1[i] = Fs_y(math.pi/2, delta_l)/m2 - g
                ax1[i] = 0.0
                
                ay2[i] = -(Fs_y(math.pi/2, delta_l)/m2 + g) 
                ax2[i] = 0.0
        elif y1[i-1] < y2[i-1]:
            if x1[i-1] < x2[i-1]:
                ay1[i] = -(Fs_y(theta, delta_l)/m1 + g) 
                ax1[i] = -Fs_x(theta, delta_l)/m1

                ay2[i] = Fs_y(theta, delta_l)/m2 - g
                ax2[i] = Fs_x(theta, delta_l)/m2
            elif x1[i-1] > x2[i-1]:
                ay1[i] = -(Fs_y(theta, delta_l)/m1 + g) 
                ax1[i] = Fs_x(theta, delta_l)/m1

                ay2[i] = Fs_y(theta, delta_l)/m2 - g
                ax2[i] = -Fs_x(theta, delta_l)/m2
            else:
                ay1[i] = -(Fs_y(math.pi/2, delta_l)/m1 + g)
                ax1[i] = 0.0
                
                ay2[i] = Fs_y(math.pi/2, delta_l)/m2 - g
                ax2[i] = 0.0
        else:
            ay1[i] = -g
            ax1[i] = -Fs_x(theta, delta_l)/m1

            ay2[i] = -g
            ax2[i] = Fs_x(theta, delta_l)/m2

    else:
        ay1[i] = -g
        ax1[i] = 0.0

        ay2[i] = -g
        ax2[i] = 0.0

    # Updating velocity
    # vy    
    if (y1[i-1] == 0):
        vy1[i] = vy1_ground + ay1[i]*delta_t
    else: 
        vy1[i] = vy1[i-1] + ay1[i]*delta_t
  
    if (y2[i-1] == 0):
        vy2[i] = vy2_ground + ay2[i]*delta_t
    else: 
        vy2[i] = vy2[i-1] + ay2[i]*delta_t
    # vx
    vx1[i] = vx1[i-1] + ax1[i]*delta_t
    vx2[i] = vx2[i-1] + ax2[i]*delta_t

    # Updating position
    y1[i] = y1[i-1] + vy1[i]*delta_t
    y2[i] = y2[i-1] + vy2[i]*delta_t

    x1[i] = x1[i-1] + vx1[i]*delta_t
    x2[i] = x2[i-1] + vx2[i]*delta_t

    # Condition if the ball hit the ground
    if (y1[i] <= 0):
        y1[i] = 0
        vy1_ground = -0.8 * vy1[i]
    if (y2[i] <= 0):
        y2[i] = 0
        vy2_ground = -0.8 * vy2[i]

    # Updating string length and theta
    l[i] = math.sqrt((x1[i] - x2[i])**2 + (y1[i] - y2[i])**2)
    if l[i] < l[0]*0.9:
        l[i] = l[0]*0.9
    elif l[i] > l[0]*1.1:
        l[i] = l[0]*1.1
    
    delta_l = abs(l[i]-l[0])

    if x1[i]-x2[i] == 0:
        theta = math.pi/2
    else:
        theta = math.atan(abs((y1[i] - y2[i])/(x1[i]-x2[i])))

    i = i + 1

    # Loop break condition
    if (abs(vy1[i-1]) < epsilon and abs(y1[i-1])) and (abs(vy2[i-1]) < epsilon and abs(y2[i-1]) < epsilon):
        break
    # elif i > 10000:
    #     break

def animate(i):
    plt.xlabel("x")
    plt.ylabel("y")
    plot = plt.plot([x1[i], x2[i]], [y1[i], y2[i]], 'ob-')
    return plot

fig = plt.figure()
plt.ylim(min(min(y1), min(y2), -0.25), max(max(y1), max(y2)))
# plt.xlim (min(min(x1), min(x2), 0), max(max(x1), max(x2)))
plt.xlim(0,8)
anim = FuncAnimation(fig, animate, frames=len(t), interval = 1, repeat = False, blit = True)
plt.show()
print("Done!")

print("Waktu yang dibutuhkan agar kedua partikel berhenti adalah", t[-1], "s")
print("Ketinggian akhir partikel 1", y1[-1])
print("Ketinggian akhir partikel 2", y2[-1])