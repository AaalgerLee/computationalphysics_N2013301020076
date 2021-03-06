import math
import matplotlib.pyplot as plt
from matplotlib import animation

#some constants that may be in need of
G=4*math.pi**2
ms=1
me=3*10**(-6)
mj=1.9*10**(-3)/2
Gs=G*ms

def StaSun(ME,MJ,dt,T):#the sun is stationary
    Gj=G*MJ
    Ge=G*ME
    re=[[]for i in range(2)]
    rj=[[]for i in range(2)]
    ve=[[]for i in range(2)]
    vj=[[]for i in range(2)]

    re[0].append(1.00)#initial condition: re=[[1.00],[0.00]]...rj=[[5.20],[0.00]]...ve=[[0],[2*math.pi]]...vj=[[0],[2*math.pi/math.sqrt(5.2)]
    re[1].append(0.00)
    rj[0].append(5.20)
    rj[1].append(0.00)
    ve[0].append(0.)
    ve[1].append(2*math.pi)
    vj[0].append(0.)
    vj[1].append(2*math.pi/math.sqrt(5.2))
    
    for i in range(int(T/dt)):
        de=math.sqrt(re[0][-1]**2+re[1][-1]**2)
        dj=math.sqrt(rj[0][-1]**2+rj[1][-1]**2)
        dej=math.sqrt((re[0][-1]-rj[0][-1])**2+(re[1][-1]-rj[1][-1])**2)

        ve[0].append(ve[0][-1]+(-G*re[0][-1]/de**3+Gj*(rj[0][-1]-re[0][-1])/dej**3)*dt)
        ve[1].append(ve[1][-1]+(-G*re[1][-1]/de**3+Gj*(rj[1][-1]-re[1][-1])/dej**3)*dt)
        vj[0].append(vj[0][-1]+(-Gs*rj[0][-1]/dj**3+Ge*(re[0][-1]-rj[0][-1])/dej**3)*dt)
        vj[1].append(vj[1][-1]+(-Gs*rj[1][-1]/dj**3+Ge*(re[1][-1]-rj[1][-1])/dej**3)*dt)

        re[0].append(re[0][-1]+ve[0][-1]*dt)
        re[1].append(re[1][-1]+ve[1][-1]*dt)
        rj[0].append(rj[0][-1]+vj[0][-1]*dt)
        rj[1].append(rj[1][-1]+vj[1][-1]*dt)

    return re,rj

n=input('the mass of Jupiter divided by its real mass is=')#change the mass of a planet right heren=1,10,100,300,400,1000
ME,MJ = me,n*mj

re,rj=StaSun(ME,MJ,0.001,15)
plt.plot(rj[0],rj[1],label='Jupiter')
plt.plot(re[0],re[1],label='Earth')
plt.title(r'Fig.Three-body Simulation,%s$m_J$'%(MJ/mj))
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.text(-6,3.6,r'Mass of Jupiter=%s$m_J$'%(MJ/mj)+'\nMass of Earth=%s$m_E$'%(ME/me)+'\nMass of Sun=$m_S$'+'\ndt=0.001,T=15')
plt.legend()
plt.xlim(-6.2,6.2)
plt.ylim(-6.2,6.2)
plt.grid()
plt.show()




# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(-6.2,6.2), ylim=(-6.2,6.2))
line, = ax.plot([], [],lw=1,label='Jupiter') 
line1, = ax.plot([], [],lw=1,label='Earth') 
plt.title('Three-Body Simulation-the Sun Is Stationary')
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.grid(True,color='k')
plt.legend()
note = ax.text(-6,3.6,'')

# initialization function: plot the background of each frame
def init():  
    line.set_data([], []) 
    line1.set_data([],[])
    note.set_text('') 
    return line,line1,note
# animation function.  this is called sequentially   
def animate(j):
    ME=me
    MJ=mj*10*j
    re,rj=StaSun(ME,MJ,0.001,15)
    line.set_data(rj[0],rj[1])
    line1.set_data(re[0],re[1]) 
    note.set_text(r'Mass of Jupiter=%d$m_J$'%(MJ/mj)+'\nMass of Earth=%d$m_E$'%(ME/me)+'\nMass of Sun=$m_S$'+'\ndt=0.001,T=15')
    return line,line1,note
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=130, interval=50)
#anim1.save('/home/shangguan/ex12/animation1/haha.png')
plt.show()  









