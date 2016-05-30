import matplotlib.pyplot as plt
from matplotlib import animation 

def loren(x0,y0,z0,r,sigma,b,dt,T):
    location=[[]for i in range(4)]
    location[0].append(x0)
    location[1].append(y0)
    location[2].append(z0)
    location[3].append(0)
    while location[3][-1]<=T:
        location[0].append(location[0][-1]+sigma*(location[1][-1]-location[0][-1])*dt)
        location[1].append(location[1][-1]+(-location[0][-2]*location[2][-1]+r*location[0][-2]-location[1][-1])*dt)
        location[2].append(location[2][-1]+(location[0][-2]*location[1][-2]-b*location[2][-1])*dt)
        location[3].append(location[3][-1]+dt)
    return location#x,y,z,time

sigma,b,dt,T=10,8./3,0.0001,50
# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(-26, 26), ylim=(-1,63))
line, = ax.plot([], [],lw=1)  
plt.title('Fig. Lorentz Model')
plt.xlabel('x')
plt.ylabel('z')
note = ax.text(12,8,'',fontsize=12)
# initialization function: plot the background of each frame
def init():  
    line.set_data([], []) 
    note.set_text('') 
    return line,note
# animation function.  this is called sequentially   
def animate(j):
    d=loren(1,0,0,j,sigma,b,dt,T)
    line.set_data(d[0],d[2]) 
    note.set_text(r'$x_0=1,y_0=0,z_0=0$'+'\n$\sigma=10,b=8/3,T=50$'+'\n$r=%s$'%j)
    return line,note

anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=40, interval=10) 
#anim1.save('/home/shangguan/computationalphysics_N2013301020076/ex10/anim1/haha.png')
plt.show()  

