#this project is to calculate ninlinear pendulum with Euler-Cromer method, 2-order Runge-Kutta method and Verlet method
import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 

def f(theta,l):
    return -g*math.sin(theta)/l
dt=0.001

#Euler-Cromer method
def EC(omega0,theta0,l,T):
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+f(theta,l)*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion
#2-order Runge-Kutta method
def RK(omega0,theta0,l,T):
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega1 = omega+f(theta,l)*dt/2
        theta1 = theta+omega*dt/2
        t1 = t+dt/2
        omega=omega+f(theta1,l)*dt
        theta=theta+omega1*dt
        t=t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion
#Verlet method
def Verlet(omega0,theta0,l,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    motion[1].append(theta0+omega0*dt)
    motion[2].append(dt)
    for i in range(1,int(T/dt)):
        motion[1].append(2*motion[1][i]-motion[1][i-1]+f(motion[1][i],l)*dt**2)
        motion[0].append((motion[1][i+1]-motion[1][i-1])/(2*dt))
        motion[2].append(motion[2][i]+dt)
    return motion


d=RK(0,2,1,10)
plt.plot(d[2],d[1],label='V2')
d=Verlet(0,3,1,10)
plt.plot(d[2],d[1],label='V4')


plt.grid(True,color='k')
plt.title('Fig.3 Nonlinear Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()



