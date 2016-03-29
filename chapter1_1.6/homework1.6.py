#assign values to the parameters
from pylab import*
n=N=float(1)
print('initial population=1 unit')
a=float(input('the birth term a/year='))
b=float(input('the death term b/year='))
time_interval=float(input('time interval/year='))
final_time=float(input('final time/year='))
#calculation
t,time,population=0,[],[]
time.append(t)
population.append(N)

for i in range(int(final_time/time_interval)):
    t=t+time_interval
    N=N+(a*N-b*N*N)*time_interval
    if N<0: #in case that the population is a negative number
        N=0
    time.append(t)
    population.append(N)
#calculate the result mathematically and accurately
math_t=np.linspace(0,final_time,int(final_time/time_interval)+1,endpoint=True)
if (b*n-a)!=0:
    c=n/(b*n-a)
    math_pop=a*c*exp(a*math_t)/(-1+b*c*exp(a*math_t))
else:
    math_pop=n+0*math_t
plot2,=plot(math_t,math_pop,color='red',linestyle='-.',linewidth=2.0,label='math result')

#plot
plot1, =plot(time,population,color='blue',linestyle='-',linewidth=3.0,label='population')
title('Population Modeling')
xlabel('time/year')
ylabel('number of individuals/unit')
legend()
show()
