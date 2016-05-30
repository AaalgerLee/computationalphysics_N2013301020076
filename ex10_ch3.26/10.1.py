import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
#Figure1 z VS time for different r
A=loren(1,0,0,5,sigma,b,dt,T)
B=loren(1,0,0,10,sigma,b,dt,T)
C=loren(1,0,0,15,sigma,b,dt,T)
D=loren(1,0,0,25,sigma,b,dt,T)

plt.figure(figsize=(14,7))
plt.subplot(1,2,1)
plt.plot(A[3],A[1],linestyle='-',linewidth=1.0,label='r=5')
plt.plot(B[3],B[1],linestyle='-',linewidth=1.0,label='r=10')
plt.plot(C[3],C[1],linestyle='-',linewidth=1.0,label='r=15')
plt.plot(D[3],D[1],linestyle='-',linewidth=1.0,label='r=25')
plt.title('Fig.1.1 Lorentz Model:y versus time')
plt.xlim(0,T)
plt.xlabel('time',fontsize=15)
plt.ylabel('y',fontsize=15)
plt.legend()

plt.subplot(1,2,2)
plt.plot(A[3],A[2],linestyle='-',linewidth=1.0,label='r=5')
plt.plot(B[3],B[2],linestyle='-',linewidth=1.0,label='r=10')
plt.plot(C[3],C[2],linestyle='-',linewidth=1.0,label='r=15')
plt.plot(D[3],D[2],linestyle='-',linewidth=1.0,label='r=25')
plt.title('Fig.1.2 Lorentz Model:z versus time')
plt.xlim(0,T)
plt.xlabel('time',fontsize=15)
plt.ylabel('z',fontsize=15)
plt.legend()
plt.show()

#Figure2 phase-space plot
D=loren(1,0,0,25,sigma,b,dt,T)
plt.figure(figsize=(14,5.5))
plt.subplot(1,3,1)#
plt.plot(D[0],D[1],linestyle='-',linewidth=1.0)
plt.title('Fig.2.1 Phase Space plot:y VS x,r=25')
plt.xlabel('x',fontsize=15)
plt.ylabel('y',fontsize=15)
plt.subplot(1,3,2)#
plt.plot(D[0],D[2],linestyle='-',linewidth=1.0)
plt.title('Fig.2.2 Phase Space plot:z VS x,r=25')
plt.xlabel('x',fontsize=15)
plt.ylabel('z',fontsize=15)
plt.subplot(1,3,3)#
plt.plot(D[1],D[2],linestyle='-',linewidth=1.0)
plt.title('Fig.2.3 Phase Space plot:z VS y,r=25')
plt.xlabel('y',fontsize=15)
plt.ylabel('z',fontsize=15)
plt.show()

#Figure3 draw the 3D figure
fig = plt.figure()
ax=Axes3D(fig)     
ax.plot(D[0],D[1],D[2], linestyle='-', linewidth=1.0,label='r=25')
ax.set_title('Fig.2.4 Lorentz Model, r=25')
ax.set_xlabel('x')
ax.set_ylabel('y') 
ax.set_zlabel('z')
plt.show()




