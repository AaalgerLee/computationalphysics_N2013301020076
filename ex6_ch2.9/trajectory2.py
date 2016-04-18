print ('This is the trajectory with air resistence, which is only related to the velocity of cannon.')
import math
v=input('firing velocity(m/s)=')
angle=input('firing angle(??du??)=')
B=input('constant related to air drag(m^-1)=')
dt=0.01
v_x=v * math.cos(angle * math.pi/180)
v_y=v * math.sin(angle * math.pi/180)
x,y,t=0,0,0
distance_x, distance_y=[],[]
distance_x.append(x)
distance_y.append(y)
a_x2=-B*v*v_x
a_y2=-9.8-B*v*v_y
while y>= 0:
    x=x+v_x*dt
    v_x=v_x+a_x2*dt
    y=y+v_y*dt
    v_y=v_y+a_y2*dt
    t=t+dt
    v=(v_x ** 2 + v_y ** 2) ** 0.5
    a_x2=-B*v*v_x
    a_y2=-9.8-B*v*v_y
    distance_x.append(x)
    distance_y.append(y)
#plot the figure
from pylab import*
plot(distance_x,distance_y,color='green',linestyle='-',linewidth=3.0,label='??')
grid(True,color='k')
title('Trajectory of cannon shell')
xlabel('horizon distance(m)')
ylabel('vertical distance(m)')
legend()
show()

