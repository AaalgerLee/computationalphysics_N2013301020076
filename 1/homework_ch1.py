#assign values to the parameters
A=input('initial number of particle A=')
B=input('initial number of particle B=')
tau_A=input('decay time constant for A particle tao_A =')
tau_B=input('decay time constant for B particle tao_ B=')
time_interval=input('time_interval=')
final_time=input('final_time=')
#caculate
t=0
ymax=0
xmax=final_time
time=[]
NA=[]
NB=[]
time.append(t)
NA.append(A)
NB.append(B)
for i in range(int(final_time/time_interval)+1):
    t=t+time_interval
    B=B+(A/tau_A-B/tau_B)*time_interval
    A=A-(A/tau_A)*time_interval    
    if A>B:
        if ymax<A:
            ymax=A
        else:
            ymax=ymax
    else:
        if ymax<B:
            ymax=B
        else:
            ymax=ymax
    time.append(t)
    NA.append(A)
    NB.append(B)

#draw the picture
from pylab import*
plot1, =plot(time,NA,color='green',linestyle='-',linewidth=1.0,label='Number of A')
plot2, =plot(time,NB,color='blue',linestyle='-',linewidth=1.0,label='Number of B')

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
grid(True,color='k')

#label the title and axis
title('The Number of A and B In the Decay')
xlabel('Time')
ylabel('Number of The Nuclei')

#add figure legends
#legend(handles=[plot1,plot2])
legend()
#waiting to be done:make the mark semi-transparent if it is blocked by the graph
#for label in ax.get_xticklabels()+ax.get_ytick;ables():
#    label.set_fontsize(16)
#    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.06))
#mark certain point

show()

