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
        B=0.0039 + 0.0058/(1+math.exp((v-35)/5))
        v_x1=v_x - B * v * v_x * dt + 0.00041 * (omegay*v_z - omegaz*v_y) * dt  
        v_y1=v_y - B * v * v_y * dt + 0.00041 * (omegaz*v_x - omegax*v_z) * dt- 9.8 * dt 
        v_z1=v_z - B * v * v_z * dt + 0.00041 * (omegax*v_y - omegay*v_x) * dt
        v_x,v_y,v_z=v_x1,v_y1,v_z1
        v=math.sqrt(v_x**2 + v_y**2 + v_z**2)
        distance[0].append(x)   
        distance[1].append(y)
        distance[2].append(z)
    return distance
#FIGURE.1: draw a figure illustrating the deflection of each direction, just like fig.2.9 on the textbook
pitcher=[[0]*15,[]]
home=[[20]*15,[]]
for i in range(15):
    pitcher[1].append(0.1*i-0.1)
    home[1].append(0.1*i-0.1)  
d=Trajectory(30,5,0,30,0)
plt.plot(d[0],d[1],linestyle='-',linewidth=1.0)
plt.plot(d[0],d[2],linestyle='-',linewidth=1.0)
plt.plot(pitcher[0],pitcher[1],linestyle='--',linewidth=0.8)
plt.plot(home[0],home[1],linestyle='--',linewidth=0.8)
plt.xlim(-1,25)
plt.annotate('pitcher', xy = (0,0.1), xytext = (3,0.2),arrowprops = dict(facecolor = 'black'),fontsize=14)
plt.annotate('home plate', xy = (20,0.1), xytext = (12,0.2),arrowprops = dict(facecolor = 'black'),fontsize=14)
plt.annotate('vertical deflection(y)', xy = (d[0][20],d[1][20]), xytext = (6,1.),arrowprops = dict(facecolor = 'black'),fontsize=16)
plt.annotate('horizontal deflection(z)', xy = (d[0][20],d[2][20]), xytext = (8,0.3),arrowprops = dict(facecolor = 'black'),fontsize=16)
plt.title('Fig.1 Deflection of Sidearm Curve Ball')
plt.xlabel('Horizon Distance x(m)')
plt.ylabel('y or z (m)')
plt.show()

#FIGURE.2:Draw the 2D figure of various firing angles
for j in range(7):
    d=Trajectory(30,40+3*j,0,20,0)
    plt.plot(d[0],d[1], linestyle='-', linewidth=1.0, label='firing angle:%d'%(40+3*j) + r'$^{\circ}$')
plt.grid(True,color='k')
plt.title('Fig.2 Motion of Batted Ball of various firing angles')
plt.xlabel('Horizon Distance x(m)')
plt.ylabel('y or z (m)')
plt.ylim(0,30)
plt.legend()
plt.show()

#FIGURE.3:Draw the 2D figure of various angular velocities
d1=Trajectory(30,30,20,0,0)
d2=Trajectory(30,30,0,20,0)
d3=Trajectory(30,30,0,0,20)
d4=Trajectory(30,30,200,0,0)
d5=Trajectory(30,30,0,200,0)
d6=Trajectory(30,30,0,0,200)

ax1=plt.subplot(1,2,1)
plt.plot(d1[0],d1[1], linestyle='-', linewidth=1.0, label='omega:(20,0,0)rps' )
plt.plot(d2[0],d2[1], linestyle='-', linewidth=1.0, label='omega:(0,20,0)rps' )
plt.plot(d3[0],d3[1], linestyle='-', linewidth=1.0, label='omega:(0,0,20)rps' )
plt.plot(d4[0],d4[1], linestyle='-', linewidth=1.0, label='omega:(200,0,0)rps' )
plt.plot(d5[0],d5[1], linestyle='-', linewidth=1.0, label='omega:(0,200,0)rps' )
plt.plot(d6[0],d6[1], linestyle='-', linewidth=1.0, label='omega:(0,0,200)rps' )
plt.grid(True,color='k')
plt.title('Fig3.1Horizontal Deflection V.S. omega')
plt.xlabel('Horizon Distance x(m)')
plt.ylabel('y (m)')
ax1.legend(loc='lower left') 

ax2=plt.subplot(1,2,2)
plt.plot(d1[0],d1[2], linestyle='-', linewidth=1.0, label='omega:(20,0,0)rps')
plt.plot(d2[0],d2[2], linestyle='-', linewidth=1.0, label='omega:(0,20,0)rps' )
plt.plot(d3[0],d3[2], linestyle='-', linewidth=1.0, label='omega:(0,0,20)rps' )
plt.plot(d4[0],d4[2], linestyle='-', linewidth=1.0, label='omega:(200,0,0)rps' )
plt.plot(d5[0],d5[2], linestyle='-', linewidth=1.0, label='omega:(0,200,0)rps' )
plt.plot(d6[0],d6[2], linestyle='-', linewidth=1.0, label='omega:(0,0,200)rps' )
plt.grid(True,color='k')
plt.title('Fig3.2Horizontal Deflection V.S. omega')
plt.xlabel('Horizon Distance x(m)')
plt.ylabel('z (m)')
plt.legend()
ax2.legend(loc='lower left') 
plt.show()

#FIGURE4 draw the 3D figure
fig = plt.figure()
ax=Axes3D(fig)   #ax = fig.add_subplot(111, projection='3d')  
ax.plot(d1[2],d1[0],d1[1], linestyle='-', linewidth=1.0, label='omega:(20,0,0)rps')
ax.plot(d2[2],d2[0],d2[1], linestyle='-', linewidth=1.0, label='omega:(0,20,0)rps' )
ax.plot(d3[2],d3[0],d3[1], linestyle='-', linewidth=1.0, label='omega:(0,0,20)rps' )
ax.plot(d4[2],d4[0],d4[1], linestyle='-', linewidth=1.0, label='omega:(200,0,0)rps' )
ax.plot(d5[2],d5[0],d5[1], linestyle='-', linewidth=1.0, label='omega:(0,200,0)rps' )
ax.plot(d6[2],d6[0],d6[1], linestyle='-', linewidth=1.0, label='omega:(0,0,200)rps' )
#ax.plot(0,0,1, linestyle='star')
#ax.scatter(type1_x, type1_y, s=20, c='red')zdir='y'
ax.scatter(0, 0, 1, marker='*',s=120,color='red',label='pitcher')
 
ax.legend(loc='upper left')
ax.set_title('     Fig.4 Motion in 3-dimension')
ax.set_xlabel('Horizon Deflection z(m)')
ax.set_ylabel('HorizontalDistance x(m)') 
ax.set_zlabel('Vertical Deflection y(m)')
ax.set_xlim(-7,2)
ax.set_ylim(0,70)
ax.set_zlim(0,12)
plt.show()





