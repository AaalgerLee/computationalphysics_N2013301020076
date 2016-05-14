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

#Fig.1.damped pendulum without driving force
d=DampedDriven(0,0.2,1,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=1')
d=DampedDriven(0,0.2,3,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=3')
d=DampedDriven(0,0.2,9.8**0.5*2,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q='+r'$2\sqrt{g/l}$')
d=DampedDriven(0,0.2,10,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=10')
d=DampedDriven(0,0.2,30,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=30')
plt.xlim(0,10)
plt.grid(True,color='k')
plt.title('Fig.1 Damped Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()

#Fig.2 damped driven pendulum, also known as linear forced pendulum.(omega0=0,theta0=0.2,q=1,FD=0.4or0.8or2,,omegaD=2,l=1,T=20
d=DampedDriven(0,0.2,1,0.4,1,1,20)#(omega0,theta0,q,FD,omegaD,l,T)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.4,\Omega_D=1$')
d=DampedDriven(0,0.2,1,0.4,2,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.4,\Omega_D=2$')
d=DampedDriven(0,0.2,1,0.8,2,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.8,\Omega_D=2$')
d=DampedDriven(0,0.2,1,2,2.0,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=2.0,\Omega_D=2$')
plt.text(13,-0.35,r'$\theta_0=0.2,q=1,l=1$')
plt.xlim(0,20)
plt.title('Fig.2 Damped Driven Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.grid(True,color='k')
plt.legend()
plt.show()

#animated figure
def findmaximum(a,b):
    if a>b:
        return a
    else:
        return b

A=0
OMEGA=0
# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(0, 20), ylim=(-0.20,0.25))
line, = ax.plot([], [], lw=1.5)  
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
    dis=DampedDriven(0,0.2,1,0.2,0.1*j,1,20) #(omega0,theta0,q,FD,omegaD,l,T).dt=0.001,so the length of x,y is 20/dt=20000
    x = dis[2]  
    y = dis[1]
    amplitude=reduce(findmaximum,y[10000:])#suppose 10 seconds leter, the motion is almost periodic
    if amplitude>A:
        A,OMEGA=amplitude,0.1*j
    line.set_data(x, y) 
    note.set_text(r'$\theta_0=0.2,q=1,F_D=0.2,l=1$'+'\ndriving frequency'+r'$\Omega_D$'+':%s(Hz)'%(0.1*j)+'\namplitude:%s(rad)'%amplitude)
    note1.set_text('resonance'+'\ndriving frequency:%s(Hz)'%OMEGA+'\namplitude:%s(rad)'%A)
    return line,note,note1
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=130, interval=50)#, blit=True) 
#anim1.save('/home/shangguan/computationalphysics_N2013301020076/ex8_ch3.7/try/haha.png')
plt.show()  










