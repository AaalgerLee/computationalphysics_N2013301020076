import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
#calculate the trajectory
def DampedDriven(omega0,theta0,q,FD,omegaD,l,T):#q is related to damping force, while FD and omegaD is related to the driving force. the length of the rod is l.T is the interest time.
    dt=0.001
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+(-g*theta/l-q*omega+FD* math.sin(omegaD*t))*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

def findmaximum(a,b):
    if a>b:
        return a
    else:
        return b
A=0
OMEGA=0
# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(0, 20), ylim=(-0.25,0.25))
line, = ax.plot([], [], lw=2)  
plt.title('Damped Driven Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(rad)')
plt.grid(True,color='k')
note = ax.text(10,0.1,'',fontsize=12)
note1= ax.text(10,-0.1,'',fontsize=12,color='red')
# initialization function: plot the background of each frame
def init():  
    line.set_data([], []) 
    note.set_text('')
    note1.set_text('') 
    return line,note,note1
# animation function.  this is called sequentially   
def animate(j):
    global A,OMEGA
    dis=DampedDriven(0,0.2,1,0.2,0.1*j,1,20) #dt=0.001,so the length of x,y is 20/dt=20000
    x = dis[2]  
    y = dis[1]
    amplitude=reduce(findmaximum,y[10000:])#suppose 10 seconds leter, the motion is almost periodic
    if amplitude>A:
        A,OMEGA=amplitude,0.1*j
    line.set_data(x, y) 
    note.set_text('driving frequency'+r'$\Omega_D$'+':%s'%(0.1*j)+'\namplitude:%s'%amplitude)
    note1.set_text('max amplitude:%s'%A+'\ndriving frequency:%s'%OMEGA)
    return line,note,note1

anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=130, interval=50)#, blit=True) 
#anim1.save('/home/shangguan/computationalphysics_N2013301020076/ex8_ch3.7/try/haha.png')
plt.show()  







