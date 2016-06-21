#this project is to calculate ninlinear pendulum with Euler-Cromer method
import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
dt=0.02

#Euler-Cromer method, only nonlinearity
def EC(omega0,theta0,l,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        motion[0].append(motion[0][-1]-g*math.sin(motion[1][-1])*dt/l)
        motion[1].append(motion[1][-1]+motion[0][-1]*dt)
        motion[2].append(motion[2][-1]+dt)
    return motion#omega,theta,time

#find out the amplitude
def Amplitude(y):
    return (max(y[int(len(y)/2):]) - min(y[int(len(y)/2):]))/2

#find out the period
def Period(x):
    k=[]
    for i in range(int(len(x[1])/2),len(x[1])):
        if x[1][i-1]<=0 and x[1][i]>0:
            k.append(x[2][i-1])
    return (k[-1]-k[0])/(len(k)-1)
        

#fig.3 EC method to figure out the relationship between amplitude and period
d=EC(0,1,1,20)
plt.plot(d[2],d[1],linestyle='-',label=r'$\theta_0=1$')
d=EC(0,2,1,20)
plt.plot(d[2],d[1],linestyle='-',label=r'$\theta_0=2$')
d=EC(0,3,1,20)
plt.plot(d[2],d[1],linestyle='-',label=r'$\theta_0=3$')
plt.title(r'Nonlinear Pendulum V.S. $\theta_0$')
plt.text(15,-3.5,'rod length l=1.0'+'\ntime step dt=0.02s')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.xlim(0,20)
plt.grid(True)
plt.legend()
plt.show()

# Fig4. amplitude vs period
A,T,Theta=[],[],[]
for i in range(1,60):
    d=EC(0,0.05*i,1,20)
    Theta.append(0.05*i)
    A.append(Amplitude(d[1]))
    T.append(Period(d))
plt.plot(A,T,linestyle='-',label='amplitude VS period')
plt.title('Nonlinear Pendulum-amplitude V.S. period')
plt.xlabel('Amplitude(rad)')
plt.ylabel('Period(second)')
plt.text(1.8,4,'rod length l=1.0'+'\ntime step dt=0.02s')
plt.grid(True)
plt.legend()
plt.show()
    






