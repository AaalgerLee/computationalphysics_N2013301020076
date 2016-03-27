#assign values to the parameters
A0=A=100
tau_A=1
print('initial number of particle A=100')
print('decay time constant for A particle tao_A/seconds =1')
B0=B=input('initial number of particle B=')
tau_B=input('decay time constant for B particle tao_ B/seconds=')
time_interval=input('time_interval/seconds=')
final_time=input('final_time/seconds=')
import math
#caculate
t=0
if A>B:
    ymax=A
else:
    ymax=B
xmax=final_time
time=[]
NA=[]
NB=[]
time.append(t)
NA.append(A)
NB.append(B)
math_NA=[]
math_NB=[]
math_NA.append(A0*math.exp(-t))
math_B=tau_B*A0*math.exp(-t)/(tau_A-tau_B)+(B0-tau_B*A0/(tau_A-tau_B))*math.exp(-t/tau_B)
math_NB.append(math_B)

for i in range(int(final_time/time_interval)+1):
    t=t+time_interval
    B=B+(A/tau_A-B/tau_B)*time_interval
    A=A-(A/tau_A)*time_interval    
    if A>B:
        if ymax<A:
            ymax=A
    else:
        if ymax<B:
            ymax=B
    time.append(t)
    NA.append(A)
    NB.append(B)
    math_NA.append(A0*math.exp(-t))
    math_B=tau_B*A0*math.exp(-t)/(tau_A-tau_B)+(B0-tau_B*A0/(tau_A-tau_B))*math.exp(-t/tau_B)
    math_NB.append(math_B)
#draw the picture
from pylab import*
plot1, =plot(time,NA,color='green',linestyle='-',linewidth=3.0,label='Number of A')
plot2, =plot(time,NB,color='blue',linestyle='-',linewidth=3.0,label='Number of B')
plot3,=plot(time,math_NA,color='m',linestyle='-.',linewidth=2.0,label='math A')
plot4,=plot(time,math_NB,color='y',linestyle='-.',linewidth=2.0,label='math B')
#mark several figures on the axis
xticks(np.linspace(0,xmax,6,endpoint=True))
xticks([0,xmax/5,xmax*2/5,xmax*3/5,xmax*4/5,xmax])
yticks(np.linspace(0,ymax,5,endpoint=True))
yticks([0,ymax/4,ymax/2,ymax*3/4,ymax])

#set the boundary of the axis
dx=final_time*0.1
dy=ymax*0.1
xlim(0-dx,xmax+dx)
ylim(0-dy,ymax+dy)

#add the net
grid(True,color='k')

#label the title and axis
title('The Number of A and B In the Decay')
xlabel('Time')
ylabel('Number of The Nuclei')

#add figure legends
legend()
#waiting to be done:make the mark semi-transparent if it is blocked by the graph
#for label in ax.get_xticklabels()+ax.get_ytick;ables():
#    label.set_fontsize(16)
#    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.06))
#mark certain point

show()
