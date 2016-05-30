import matplotlib.pyplot as plt

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


def poincare(zero,non1,non2,k):
    poi=[[]for i in range(2)]
    for i in range(300000,len(zero)-1):
        if (zero[i]-k)*(zero[i+1]-k)<=0:
            poi[0].append(non1[i])
            poi[1].append(non2[i])
    return poi

sigma,b,dt,T=10,8./3,0.0001,200
D=loren(1,0,0,25,sigma,b,dt,T)

#Figure 3.1 poincare section r=25
plt.subplot(1,2,1)#x=0
poix=poincare(D[0],D[1],D[2],0)
plt.scatter(poix[0],poix[1],s=10)
plt.title('Fig.3.1 Lorentz Model, Poincare Section,r=25')
plt.xlabel('y',fontsize=20)
plt.ylabel('z',fontsize=20)
plt.text(0,10.5,'phase space plot when x=0')

plt.subplot(1,2,2)#y=0
poiy=poincare(D[1],D[0],D[2],0)
plt.scatter(poiy[0],poiy[1],s=10)
plt.title('Fig.3.2 Lorentz Model, Poincare Section:r=25')
plt.xlabel('x',fontsize=20)
plt.ylabel('z',fontsize=20)
plt.text(0,11,'phase space plot when y=0')
plt.show()

#Figure 3.3 poincare section r=25
plt.subplot(2,2,1)#x=2
poix=poincare(D[0],D[1],D[2],2)
plt.scatter(poix[0],poix[1],s=10)
plt.title('Fig.3.3 Poincare Section,r=25')
plt.xlabel('y')
plt.ylabel('z')
plt.text(0,4,'Lorentz Model'+'\nphase space plot when x=2')

plt.subplot(2,2,2)#x=-2
poix=poincare(D[0],D[1],D[2],-2)
plt.scatter(poix[0],poix[1],s=10)
plt.title('Fig.3.4 Poincare Section,r=25')
plt.xlabel('y')
plt.ylabel('z')
plt.text(0,4,'Lorentz Model'+'\nphase space plot when x=-2')

plt.subplot(2,2,3)#y=2
poiy=poincare(D[1],D[0],D[2],2)
plt.scatter(poiy[0],poiy[1],s=10)
plt.title('Fig.3.5 Poincare Section:r=25')
plt.xlabel('x')
plt.ylabel('z')
plt.text(0,3,'Lorentz Model'+'\nphase space plot when y=2')

plt.subplot(2,2,4)#y=-2
poiy=poincare(D[1],D[0],D[2],-2)
plt.scatter(poiy[0],poiy[1],s=10)
plt.title('Fig.3.6 Poincare Section:r=25')
plt.xlabel('x')
plt.ylabel('z')
plt.text(0,3,'Lorentz Model'+'\nphase space plot when y=-2')
plt.show()


D=loren(1,0,0,35,sigma,b,dt,T)
#Figure3.3 poincare section,r=35
plt.subplot(1,2,1)#x=0
poix=poincare(D[0],D[1],D[2],0)
plt.scatter(poix[0],poix[1],s=10)
plt.title('Fig.3.7 Lorentz Model, Poincare Section')
plt.xlabel('y',fontsize=20)
plt.ylabel('z',fontsize=20)
plt.text(0,16,'r=35'+'\nphase space plot when x=0')

plt.subplot(1,2,2)#y=0
poiy=poincare(D[1],D[0],D[2],0)
plt.scatter(poiy[0],poiy[1],s=10)
plt.title('Fig.3.8 Lorentz Model, Poincare Section')
plt.xlabel('x',fontsize=20)
plt.ylabel('z',fontsize=20)
plt.text(1,17,'r=35'+'\nphase space plot when y=0')
plt.show()


















