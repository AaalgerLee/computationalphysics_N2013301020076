import math
import matplotlib.pyplot as plt       
from mpl_toolkits.mplot3d import Axes3D  # for 3D plot 
#calculate the trajectory,the SI unit is involved
def Trajectory(v,theta,omegax,omegay,omegaz):
    v_x,v_y,v_z=v*math.cos(theta*math.pi/180), v*math.sin(theta*math.pi/180), 0
    x,y,z=0,1,0   # suppose the y=0 cprresponds to the ground while y=1meter the initial height to fire the ball
    dt=0.01
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
    distance[2].append(z)
    while y>=0:
        x=x+v_x*dt
        y=y+v_y*dt
        z=z+v_z*dt
        B=0.0039 + 0.0058/(1+math.exp((v_y-35)/5))
        v_x1=v_x - B * v * v_x * dt + 0.00041 * (omegay*v_z - omegaz*v_y) * dt  
        v_y1=v_y - B * v * v_y * dt + 0.00041 * (omegaz*v_x - omegax*v_z) * dt- 9.8 * dt 
        v_z1=v_z - B * v * v_z * dt + 0.00041 * (omegax*v_y - omegay*v_x) * dt
        v_x,v_y,v_z=v_x1,v_y1,v_z1
        v=math.sqrt(v_x**2 + v_y**2 + v_z**2)
        distance[0].append(x)   
        distance[1].append(y)
        distance[2].append(z)
    return distance
#Draw the 2D figure
d=Trajectory(30,10,0,0,0)
plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label='angular velocity:0')
d=Trajectory(30,10,0,15,0)
plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label='angular velocity:100')
d=Trajectory(30,10,0,1000,0)
plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label='angular velocity:300')
    #plt.plot(d[0],d[2],linestyle='-',linewidth=1.0,label='horizontal deflection')    


plt.grid(True,color='k')
plt.title('Motion of Batted Ball')
plt.xlabel('Horizon Distance x(m)')
plt.ylabel('y or z (m)')
plt.legend()
plt.show()
#draw the 3D figure

#def plot3d(v,theta,omega):
#    d3=Trajectory(v,theta,0,30,0)
#    fig = plt.figure()
#    ax=Axes3D(fig)   #ax = fig.add_subplot(111, projection='3d') 
#    ax.plot(d3[0],d3[2],d3[1])   
#    ax.legend()
#    ax.set_xlabel('Horizon Distance x(m)')
#    ax.set_ylabel('z(m)')
#    ax.set_zlabel('Vertical Distance y(m)')

#plt.show()





