import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
dt=0.01
#2-order Runge-Kutta method
def RK(omega0,theta0,l,q,FD,omegaD,T):
    t=0
    omega,theta = omega0,theta0
    def f(theta,omega,t):
        return -g*math.sin(theta)/l-q*omega+FD*math.sin(omegaD*t)
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        omega1 = omega+f(theta,omega,t)*dt/2
        theta1 = theta+omega*dt/2
        t1 = t+dt/2
        omega=omega+f(theta1,omega1,t1)*dt
        theta=theta+omega1*dt
        t=t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

d=RK(0,0.2,1,1,0,0,10)
plt.plot(d[2],d[1])
plt.show()







