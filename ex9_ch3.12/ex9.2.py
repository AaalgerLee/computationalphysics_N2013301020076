import math
import matplotlib.pyplot as plt      
g=9.8 
dt=0.01
#adjust theta to keep it in range of [-pi,+pi]
def adjust(x):
    while x>math.pi:
        x=x-2*math.pi
    while x<-math.pi:
        x=x+2*math.pi
    return x
#2-order Runge-Kutta method
def EC(omega0,theta0,q,l,FD,omegaD,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        motion[0].append(motion[0][-1]+(-g*math.sin(motion[1][-1])/l-q*motion[0][-1]+FD*math.sin(omegaD*motion[2][-1]))*dt)
        motion[1].append(motion[1][-1]+motion[0][-1]*dt)
        motion[2].append(motion[2][-1]+dt)
    return motion#omega,theta,t

omegaD,T=0.66,1000
def Poin(motion):
    poi=[[]for i in range(3)]
    for n in range(int(omegaD*T/2/math.pi)):
        number=int(round(2*n*math.pi/omegaD/dt))
        poi[0].append(motion[0][number])
        poi[1].append(motion[1][number])
        poi[2].append(motion[2][number])
    return poi

#fig.3 poincare section
d=EC(0,0.2,0.5,9.8,1.2,0.66,T)
d1=Poin(d)
plt.plot(map(adjust,d1[1]),d1[0],'.')
plt.title('Fig.3 Poincare Section of the Physical Pendulum')
plt.xlabel(r'$\theta$ (radius)')
plt.ylabel(r'$\omega$ (radius/second)')
plt.text(0,0.7,r'$\omega_0=0,\theta_0=0.2,q=0.5,l=9.8,\Omega_D=0.66$')
plt.text(1.5,0.5,r'$F_D=1.2,T=1000s$')
plt.show()






