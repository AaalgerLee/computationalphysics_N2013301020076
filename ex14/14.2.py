import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation

delta_x=0.001
c=300
delta_t=delta_x/c
r=1

x=np.linspace(0,1,int(1/delta_x)+1)

def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next

def after_n_step(y0,y1,n):#n=T/delta_t
    for i in range(n):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
    return y0,y1

# initialize y- one Gaussian wavepacket,k0,x0
k0,x0=1000,0.3
k1,x1=300,0.6
y1_initial,y2_initial,y3_initial=[],[],[]
for i in range(1+int(1/delta_x)):
    y1_initial.append(math.exp(-k0*(i*delta_x-x0)**2))
    y2_initial.append(-2*math.exp(-k1*(i*delta_x-x1)**2))
    y3_initial.append(math.exp(-k0*(i*delta_x-x0)**2)-2*math.exp(-k1*(i*delta_x-x1)**2))


# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(0, 1), ylim=(-2.01,2.01))
line1, = ax.plot([], [], lw=2.,label=r'$y_0=exp[-1000\times(x-0.3)^2]$')  
line2, = ax.plot([], [], lw=2.,label=r'$y_0=-2exp[-300\times(x-0.6)^2]$')
line3, = ax.plot([], [], lw=1.,label=r'$y_0=exp[-1000\times(x-0.3)^2]-2exp[-300\times(x-0.6)^2]$')
plt.title('Waves On A String With Fixed Ends')
plt.xlabel('x')
plt.ylabel('displacement')
plt.legend()
note = ax.text(0.05,-1.4,'',fontsize=12)#note = ax.text(0.65,0.8,'',fontsize=12)
# initialization function: plot the background of each frame
def init():  
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], []) 
    note.set_text('')
    return line1,line2,line3,note
# animation function.  this is called sequentially   
def animate(j):
    y10,y1=after_n_step(y1_initial,y1_initial,j)
    y20,y2=after_n_step(y2_initial,y2_initial,j)
    y30,y3=after_n_step(y3_initial,y3_initial,j)
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    note.set_text('\nstep n=%s'%j)#change the initial displacement accordingly
    return line1,line2,line3,note
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=401, interval=50)#, blit=True) 
#anim1.save('/home/shangguan/ex14/gif4/haha.png')
plt.show()  













