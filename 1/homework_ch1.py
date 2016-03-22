#assign values to the parameters
A=input('initial number of particle A=')
B=input('initial number of particle B=')
tao_A=input('decay time constant for A particle tao_A =')
tao_B=input('decay time constant for B particle tao_ B=')
time_interval=input('time_interval=')
final_time=input('final_time=')
#caculate
t=0
time=[]
NA=[]
NB=[]
time.append(t)
NA.append(A)
NB.append(B)
for i in range(int(final_time/time_interval)+1):
    t=t+time_interval
    B=B+(A/tao_A-B/tao_B)*time_interval
    A=A-(A/tao_A)*time_interval    
    time.append(t)
    NA.append(A)
    NB.append(B)


if NA[0]>NB[0]:
    ymax=NA[0]
else:
    ymax=NB[0]
xmax=final_time

#draw the picture
from pylab import*
plot(time,NA,color='green',linestyle='-',linewidth=1.0)
plot(time,NB,color='blue',linestyle='-',linewidth=1.0)

#mark several figures on the axis
xticks(np.linspace(0,xmax,5,endpoint=True))
xticks([0,xmax/4,xmax/2,xmax*3/4,xmax])
yticks(np.linspace(0,ymax,5,endpoint=True))
yticks([0,ymax/4,ymax/2,ymax*3/4,ymax])

#set the boundary of the axis
dx=final_time*0.1
dy=ymax*0.1
xlim(0-dx,xmax+dx)
ylim(0-dy,ymax+dy)
#add the net
grid(True)
#put the legent somewhere
legend(loc='upper right')

#waiting to be done:make the mark semi-transparent if it is blocked by the graph
#for label in ax.get_xticklabels()+ax.get_ytick;ables():
#    label.set_fontsize(16)
#    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.06))
#mark certain point

show()

