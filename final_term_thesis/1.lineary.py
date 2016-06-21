import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
#calculate the trajectory
def DampedDriven(omega0,theta0,q,FD,omegaD,l,T):#q-damping force, FD and omegaD-driving force, l-length of the rod,T-interest time
    dt=0.001
    motion=[[]for i in range(3)]#omege,theta,time
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0.)
    while motion[2][-1]<= T:
        motion[0].append(motion[0][-1]+(-g*motion[1][-1]/l-q*motion[0][-1]+FD* math.sin(omegaD*motion[2][-1]))*dt)
        motion[1].append(motion[1][-1]+motion[0][-1]*dt)
        motion[2].append(motion[2][-1]+dt)
    return motion#omege,theta,time

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
plt.title('Pendulum with Damping Force Only')
plt.xlabel('Time(second)')
plt.ylabel(r'$\theta$(radius)')
plt.text(6,-0.1,r'$\omega_o=0,\theta_o=0.2$'+'\n$l=1.0,F_D=0$',fontsize=14)
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
plt.text(12,-0.35,r'$\omega_0=0,\theta_0=0.2,q=1.0,l=1.0$',fontsize=14)
plt.xlim(0,20)
plt.title('Damped Driven Pendulum')
plt.xlabel('Time(second)')
plt.ylabel(r'$\theta$(radius)')
plt.grid(True,color='k')
plt.legend()
plt.show()












