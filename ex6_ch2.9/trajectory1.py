print ('This is the trajectory with no air resistence.')
import math
v=700
angle=input('firing angle(??du??)=')
v_x=v * math.cos(angle * math.pi/180)
v_y=v * math.sin(angle * math.pi/180)
dt=0.01
x,y,t=0,0,0
distance_x, distance_y=[],[]
distance_x.append(x)
distance_y.append(y)
a_x1, a_y1=0,-9.8
while y>= 0:
    x=x+v_x*dt
    v_x=v_x+a_x1*dt
    y=y+v_y*dt
    v_y=v_y+a_y1*dt
    t=t+dt
    distance_x.append(x)
    distance_y.append(y)
#plot the figure
import matplotlib.pyplot as plt
plt.plot(distance_x,distance_y,color='blue',linestyle='-',linewidth=1.0,label='trajectory')
plt.grid(True,color='k')
plt.title('Trajectory of cannon shell with no air drag')
plt.xlabel('horizon distance x(m)')
plt.ylabel('vertical distance y(m)')
plt.text(1,1,"initial speed=700m/s,no drag")
plt.legend()
plt.show()

