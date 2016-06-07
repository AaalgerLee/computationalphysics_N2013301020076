import math
import matplotlib.pyplot as plt

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


def RestFrameC(m1,m2,v1x0,v1y0,v2x0,v2y0,dt,T):
    v_cx=(m1*v1x0+m2*v2x0)/(m1+m2)
    v_cy=(m1*v1y0+m2*v2y0)/(m1+m2)
    rc=[[]for i in range(2)]
    for i in range(int(T/dt)+1):
        rc[0].append(v_cx*i*dt)
        rc[1].append(v_cy*i*dt)
    return rc


#series 1: m1=m2=1,dt=0.001,T=50,vy10=0.5/1.0/1.5/3./4.
m1,m2=1.,1.
dt,T=0.001,50
x10,y10,vx10,vy10=1.5,0.,0.,4.
vx20,vy20=0.,-1.

rc=RestFrameC(m1,m2,vx10,vy10,vx20,vy20,dt,T)
r1c,v1c=COMorbit1(m1,m2,x10,y10,vx10,vy10,dt,T)
r2c=COM2(m1,m2,r1c)

x1=map(lambda a,b:a+b,rc[0],r1c[0])
y1=map(lambda a,b:a+b,rc[1],r1c[1])
x2=map(lambda a,b:a+b,rc[0],r2c[0])
y2=map(lambda a,b:a+b,rc[1],r2c[1])


plt.subplot(1,2,1)
plt.plot(x1,y1,label='planet 1')
plt.plot(x2,y2,label='planet 2')
plt.plot(rc[0],rc[1],label='COM')
plt.title(r'Motion in the Rest Frame,$m_1=m_2=1$')
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.text(-78,-18,r'$\overrightarrow{x_{10}}=(%s,%s)$'%(x10,y10)+'\n$\overrightarrow{v_{10}}=(%s,%s)$'%(vx10,vy10)+'\n$\overrightarrow{v_{20}}=(%s,%s)$'%(vx20,vy20))
plt.legend()

plt.subplot(1,2,2)
plt.plot(r1c[0],r1c[1],label='planet 1')
plt.plot(r2c[0],r2c[1],label='planet 2')
plt.title(r'Motion in the COM Frame,$m_1=m_2=1$')
plt.xlabel(r'$x_c/AU$')
plt.ylabel(r'$y_c/AU$')
plt.text(-78,-78,r'$\overrightarrow{x_{10}}=(%s,%s)$'%(x10,y10)+'\n$\overrightarrow{v_{10}}=(%s,%s)$'%(vx10,vy10)+'\n$\overrightarrow{v_{20}}=(%s,%s)$'%(vx20,vy20))
plt.legend()

plt.show()


