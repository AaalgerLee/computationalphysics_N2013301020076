import math
import matplotlib.pyplot as plt
from matplotlib import animation      

G=4*math.pi**2
def COMorbit1(m1,m2,x0,y0,vx0,vy0,dt,T):
    alpha=-G*m2/(1+m1/m2)**2.
    r=[[]for i in range(2)]
    v=[[]for i in range(2)]
    r[0].append(x0)
    r[1].append(y0)
    v[0].append(vx0)
    v[1].append(vy0)
    for i in range(int(T/dt)):
        den=(r[0][-1]**2+r[1][-1]**2)**1.5#denominator
        v[0].append(v[0][-1]+alpha*r[0][-1]*dt/den)
        v[1].append(v[1][-1]+alpha*r[1][-1]*dt/den)
        r[0].append(r[0][-1]+v[0][-1]*dt)
        r[1].append(r[1][-1]+v[1][-1]*dt)
    return r,v

def COM2(m1,m2,r1):
    r2=[[]for i in range(2)]
    r2[0]=map(lambda x:-m1*x/m2,r1[0])
    r2[1]=map(lambda x:-m1*x/m2,r1[1])
    return r2

m1,m2=0.001,1#m1=1.,m2=1.1,x10=1.5
dt,T=0.001,50
x10,y10,vx10=1.,0.,0.
vx20,vy20=0.,-1.

# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(-2.0, 1.2), ylim=(-2,2))
line, = ax.plot([], [],lw=1,label='planet 1') 
line1, = ax.plot([], [],lw=1,label='planet 2') 
plt.title('Motion in the COM Frame')
plt.xlabel(r'$x_c/AU$')
plt.ylabel(r'$y_c/AU$')
plt.grid(True,color='k')
plt.legend()
note = ax.text(0.5,-1.8,'',fontsize=12)

# initialization function: plot the background of each frame
def init():  
    line.set_data([], []) 
    line1.set_data([],[])
    note.set_text('') 
    return line,line1,note
# animation function.  this is called sequentially   
def animate(j):
    r1c,v1c=COMorbit1(m1,m2,x10,y10,vx10,j*0.05,dt,T)
    r2c=COM2(m1,m2,r1c)
    line.set_data(r1c[0],r1c[1])
    line1.set_data(r2c[0],r2c[1]) 
    note.set_text(r'$m_1=0.001,m_2=1$'+'\n$\overrightarrow{x_{10}}=(1,0)$'+'\n$\overrightarrow{v_{10}}=(0,%s)$'%(j*0.05)+'\n$\overrightarrow{v_{20}}=(0,-1)$')
    
    return line,line1,note
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=160, interval=50)
anim1.save('/home/shangguan/computationalphysics_N2013301020076/ex11/COMm1=0.001/haha.png')
plt.show()  




