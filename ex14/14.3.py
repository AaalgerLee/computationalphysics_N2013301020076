import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation

delta_x=0.001
c=300
delta_t=delta_x/c
r=1
T=0.03
N=int(T*c/delta_x)
k=1000
t=np.linspace(0,T,N+1)

def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next


def motion_of_a_point(x_observe,x_excite):
    y_initial=[]           #initialize or excite the string in some point in the gaussian way
    for i in range(1+int(1./delta_x)):
        y_initial.append(math.exp(-k*(i*delta_x-x_excite)**2))
    y_observe=[]                  #calculate the displacement at x=0.05 or y(i=I,n)
    I=int(x_observe/delta_x)
    y0=y_initial
    y1=y_initial
    y_observe.append(y1[I])

    for i in range(N):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
        y_observe.append(y1[I])
    return y_observe


yx=motion_of_a_point(0.05,0.5)
plt.plot(t,yx)
plt.title('String Signal versus Time,x=0.05')
plt.xlabel('time(s)')
plt.ylabel('Signal(arbitrary units)')
plt.text(0.018,0.53,r'$y_0(x)=exp[-1000\times(x-0.5)^2]$')
plt.show()




#yo=motion_of_a_point(0.05,0.5)
p=abs(np.fft.rfft(yx))**2
f = np.linspace(0, c/delta_x/2, len(p))
plt.plot(f, p)
plt.xlim(0,3000)
plt.xlabel('Frequency(Hz)')
plt.ylabel('Power')
plt.title('Power spectrum')

plt.show()



