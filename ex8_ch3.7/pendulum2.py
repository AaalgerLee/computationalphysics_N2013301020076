#this project is to calculate ninlinear pendulum with Euler-Cromer method, 2-order Runge-Kutta method and Verlet method
import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 

def f(theta,l):
    return -g*math.sin(theta)/l
dt=0.02

#Euler method
def Euler(omega0,theta0,l,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        motion[0].append(motion[0][-1]+f(motion[1][-1],l)*dt)
        motion[1].append(motion[1][-1]+motion[0][-2]*dt)
        motion[2].append(motion[2][-1]+dt)
    return motion

#Euler-Cromer method
def EC(omega0,theta0,l,T):
    omega,theta,t = omega0,theta0,0
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
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
    while motion[2][-1]<=T:
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
#find out the amplitude
def Bigger(a,b):
    if a>b:
        return a
    else:
        return b
def Smaller(a,b):
    if a>b:
        return b
    else:
        return a
def Amplitude(y):
    return (reduce(Bigger,y[int(len(y)/2):]) - reduce(Smaller,y[int(len(y)/2):]))/2

#find out the period
def Period(x):
    k=[]
    for i in range(int(len(x[1])/2),len(x[1])):
        if x[1][i-1]<=0 and x[1][i]>0:
            k.append(x[2][i-1])
    return (k[-1]-k[0])/(len(k)-1)
        
#fig3.various methods
d=Euler(0,2,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='Euler method')
d=EC(0,2,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='EulerCromer')
d=RK(0,2,1,10)
plt.plot(d[2],d[1],linestyle='--',linewidth=1.0,label='Runge-Kutta')
d=Verlet(0,2,1,10)
plt.plot(d[2],d[1],linestyle='-.',linewidth=1.0,label='Verlet')
plt.text(2,15,r'$\theta_0=2,l=1$'+'\ntime step dt=0.02 seconds')
plt.legend()
plt.grid(True,color='k')
plt.title('Fig.3 Nonlinear Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()

#fig.4 ECmethod to figure out the relationship between amplitude and period
d=EC(0,1,1,20)
plt.plot(d[2],d[1],linestyle='-',label=r'$\theta_0=1$')
d=EC(0,2,1,20)
plt.plot(d[2],d[1],linestyle='-',label=r'$\theta_0=2$')
d=EC(0,3,1,20)
plt.plot(d[2],d[1],linestyle='-',label=r'$\theta_0=3$')
plt.title(r'Fig.4 Nonlinear Pendulum V.S. $\theta_0$')
plt.text(10,3,'rod length l=1m'+'\ntime step=0.02s')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.xlim(0,20)
plt.grid(True)
plt.legend()
plt.show()
# Fig5. amplitude vs period
A,T,Theta=[],[],[]
for i in range(1,60):
    d=EC(0,0.05*i,1,20)
    Theta.append(0.05*i)
    A.append(Amplitude(d[1]))
    T.append(Period(d))
plt.plot(A,T,linestyle='-',label='amplitude VS period')
plt.title('Fig.5 Nonlinear Pendulum-amplitude V.S. period')
plt.xlabel('Amplitude(rad)')
plt.ylabel('Period(second)')
plt.text(1.8,4,'rod length l=1m'+'\ntime step=0.02s')
plt.grid(True)
plt.legend()
plt.show()
    






