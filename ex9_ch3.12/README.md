Exercise 9 - chaos in the nonlinear, damped, driven pendulum(ex3.12/16/21)  
上官俊怡 2013301020076  
# 1.Abstract    
In this report, a physical pendulum is discussed. An external driving force, dissipation and nonlinearity are applied at the same time. Besides, Poincare section, attractor and bifurcation diagram are investigated to grasp a better undestanding of the movement of pendulum and the notation of chaos.  

# 2.Background    
- **Physicsl pendulum:**  
  We add an external driving force, dissipation and nonlinearity to the pendulum at the same time rather than discuss these ingredients separately. From this procedure, we are supposed to see: (1)it is possible for a system to be both deterministic and unpredictable and this is what the term chaos means;(2)the behavior in the chaotic regime is not completely random, but can be describe by a strange attractorin phase space.  

- **Chaos:**  
  The system to be both deterministic and unpredictable. That is, a system can obey certain determnistic laws of physics, but stil exhibit behavior that is unpredictable due to an extreme sensitivity to initial conditions.  

- **Poincare section:**  
  In the phase-space graph, plot ![](http://latex.codecogs.com/gif.latex?%5Comega) versus ![](http://latex.codecogs.com/gif.latex?%5Ctheta) only at times that are in phase with the driving force. That is, only the points with ![](http://latex.codecogs.com/gif.latex?%5COmega_Dt%3D2n%5Cpi) are displayed where n is an integer. Ihis is known as Poincare section. And it is a very useful way to plot and analyze the behavior of a dynamical system.  

- **Attractor:**  
  The trajectory of pendulum is drawn to the surface, which is known as attractor. Chaotic attractors have a frictal structure and are usually reffered to as strange attractors.  

- **Bifurcation diagram:**  
  It is a nice way to predict how the trasition from nonchaos to chaos comes about. It can be constructed in the following manner. Calculate ![](http://latex.codecogs.com/gif.latex?%5Ctheta) as a function of time, wait for 300driving periods so that the initial transients have decayed away, plot![](http://latex.codecogs.com/gif.latex?%5Ctheta) at times that were in phase with the driving forcr as a function of ![](http://latex.codecogs.com/gif.latex?F_D) to 400th drive periods. And repeat the process for various ![](http://latex.codecogs.com/gif.latex?F_D) and show the result in a figure, which is known as bifurcation diagram.  


# 3.Methodology and Solution
## 3.1 Physical Model 
Putting the ingredients together, the model is called a nonlinear, damped, driven pendulum, or the physical pendulum. First, we do not assume the small-angle approximation and thus do not expand ![](http://latex.codecogs.com/gif.latex?sin%5Ctheta) term. second, friction of the form <img src="http://chart.googleapis.com/chart?cht=tx&chl=-qd%5Ctheta%2Fdt" style="border:none;" /> and sinusoidal driving force ![](http://latex.codecogs.com/gif.latex?F_Dsin%28%5COmega_Dt%29) are introduced. Therefore, the equation of motion is:  
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%2BF_Dsin(%5COmega_Dt)" style="border:none;" />    
The above ordinary differential equation has no known exact solution.  
The natural frequency of undamped pendulum is ![](http://latex.codecogs.com/gif.latex?%5COmega%3D%5Csqrt%7Bg/l%7D)  

## 3.2 Numerical Method
**The equation of motion**  
It can be rewritten as two first-order differential equations as follows:  
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5C%5C%5Cfrac%7Bd%5Comega%7D%7Bdt%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Comega%2BF_Dsin(%5COmega_Dt)%0A%5C%5C%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%3D%5Comega" style="border:none;" />  

**Euler-Cromer Method**  
In this project, Euler-Cromer method is applied. Refer to the Appendix of the textbook, it can be deduced that:  
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5C%5C%5Comega_%7Bi%2B1%7D%3D%5Comega_i%2B%5B-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta_i-q%5Comega_i%2BF_Dsin(%5COmega_Dt_i)%5D%5CDelta%20t%0A%5C%5C%5Ctheta_%7Bi%2B1%7D%3D%5Ctheta_i%2B%5Comega_%7Bi%2B1%7D%5CDelta%20t%0A%5C%5Ct_%7Bi%2B1%7D%3Dt_i%2B%5CDelta%20t" style="border:none;" />  
or <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5C%5C%5Comega_%7Bi%2B1%7D%3D%5Comega_i%2Bf(%5Ctheta_i%2C%5Comega_i%2Ct_i)%5CDelta%20t%0A%5C%5C%5Ctheta_%7Bi%2B1%7D%3D%5Ctheta_i%2B%5Comega_%7Bi%2B1%7D%5CDelta%20t%0A%5C%5Ct_%7Bi%2B1%7D%3Dt_i%2B%5CDelta%20t" style="border:none;" /> where <img src="http://chart.googleapis.com/chart?cht=tx&chl=f(%5Ctheta%2C%5Comega%2Ct)%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Comega%2BF_Dsin(%5COmega_Dt)" style="border:none;" />   

**Adjust <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta" style="border:none;" />**  
The value of <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta" style="border:none;" /> is adjusted so as to keep it in the range <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5B-%5Cpi%2C%2B%5Cpi%5D" style="border:none;" /> . Now the pendulum is free to swing all the way around its pivot point, and values of <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta" style="border:none;" /> differed by ![](http://latex.codecogs.com/gif.latex?2%5Cpi) correspond to the same position. So this adjustment is done because for ploting purpose it is convenient to keep <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctheta" style="border:none;" /> in the range.  

# 4.Code  
Here is the code for [theta V.S.t & Phase-space Plot](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/ex9.1.py)  
Here is the code for [poincare section & bifurcation diagram](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/ex9.2.py)  

# 5.Running and Analysis
## 5.1 The Influence of ![](http://latex.codecogs.com/gif.latex?F_D)
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_1.png)  
The above figure is the behavior of the driven, damped, nonlinear pendulum in 60 seconds whose parameters are set as ![](http://latex.codecogs.com/gif.latex?%5Comega%28t%3D0%29%3D0%2C%20%5Ctheta%28t%3D0%29%3D0.2%2C%20q%3D0.5%2Cl%3D9.8%2C%20%5COmega_D%3D0.66) with ![](http://latex.codecogs.com/gif.latex?dt%3D0.04seconds). The left figures are the behavior of ![](http://latex.codecogs.com/gif.latex?%5Ctheta)as a function of time while the right are the behavior of ![](http://latex.codecogs.com/gif.latex?%5Comega).  
From the figures, the folowing conclusion can be reached. When there is no driving force,the motion is damped and the pendulum comes to rest after several oscillation, the frequency of which is close to thenatural frequency of the undamped pendulum![](http://latex.codecogs.com/gif.latex?%5COmega). With small driving force, the initial displacement of the pendulum leads to a component of the motion that decays with time and has frequency of![](http://latex.codecogs.com/gif.latex?%5COmega). After the transient is damped away, the pendulum settles into a steady oscillation with frequency the same as driving frequency![](http://latex.codecogs.com/gif.latex?%5COmega_D). At high driving amplitude, the motion is no longer simple.  

![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_1.3.png)  
This is the behavior of![](http://latex.codecogs.com/gif.latex?%5Ctheta)under![](http://latex.codecogs.com/gif.latex?F_D%3D1.2), with and without the resetting of the angle. The pendulum does not settle into any sort of repeating steady-state behavior, at least in the range shown here. In the upper figure, the vertical jumps are the result of our adjustment of![](http://latex.codecogs.com/gif.latex?%5Ctheta).   
From the figures above, it is obvious that at low driven force, the pendulum experiences simple harmonic oscillation. But at high drive, the motion is chaotic.  
## 5.2 Phase-space Plot
In this part, the trajectory of angular velocity ![](http://latex.codecogs.com/gif.latex?%5Comega) as a function of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) is demonstrated.  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_2.1.png)  
This is the results for![](http://latex.codecogs.com/gif.latex?%5Comega) as a function of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) for a pendulum in 500 seconds. The parameters are the same as in Fig 1.1 and Fig 1.2. The figure on the right is for high drive, and the horizontal jumps are due to the adjustment of ![](http://latex.codecogs.com/gif.latex?%5Ctheta).  

For the small driving force shown in the left figure above, it can be seen that there is a transient depending on the initial conditions, but the pendulum quickly settles into a regular orbit in phase space corresponding to the oscillatory motion of both ![](http://latex.codecogs.com/gif.latex?%5Ctheta) and ![](http://latex.codecogs.com/gif.latex?%5Comega). This final orbit is independent of the initial conditions. For the figure on the right, it is the behavior of pendulum in chaotic regime.The pattern is not a simple one, but it is not completely random. Meanwhile, it exhibits phase-space trajectories with significant structure.  
To have a better understanding of this figure in the chaotic regime, the Poincare Section is depicted below in Fig 3. In this graph, the points are made in a period as long as 1000 seconds while time interval is ![](http://latex.codecogs.com/gif.latex?dt%3D0.01seconds). Other parameters are the same as Fig 1.1 and can be seen in the graph.  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_2.3.png)  

## 5.3 Routes to Chaos-Bifurcation Diagram
This part deals with the question: how does the transition from simple to chaotic behacior take place?
First, we draw the results for ![](http://latex.codecogs.com/gif.latex?%5Ctheta) as a function of time with driving force a little bit different.  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_3.1.png)  
This is the results for![](http://latex.codecogs.com/gif.latex?%5theta) as a function of time for the pendulum with different drive amplitude within 100 seconds. The parameters are the same as Fig.1.1 while the time interval is ![](http://latex.codecogs.com/gif.latex?dt%3D0.01seconds).  
The left figure has a period as the drive period, the middle figure has a period twice the drive period, while the right figure has a period that is four times the drive period.  
To know this deeper, bifurcation diagram is drawn. For each value of ![](http://latex.codecogs.com/gif.latex?F_D), ![](http://latex.codecogs.com/gif.latex?%5theta) is calculated as a function of time. After waiting foe 30 driving periods so that the initial transients have decayed away, we plot ![](http://latex.codecogs.com/gif.latex?%5theta) as times that are in phase with the driving force as a function of ![](http://latex.codecogs.com/gif.latex?F_D). Here we plot the points up to the 60th drive period.  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_3.4.png)  
Motion whose period is n times the drive period will yield n points on the bifurcation diagram for that value of ![](http://latex.codecogs.com/gif.latex?F_D). From the diagram above, we know that the period is ![](http://latex.codecogs.com/gif.latex?T_D) up to approximately ![](http://latex.codecogs.com/gif.latex?F_D%3D1.402), followed by a transition to period-![](http://latex.codecogs.com/gif.latex?2T_D) motion up to ![](http://latex.codecogs.com/gif.latex?F_D%3D1.437). The motion with period ![](http://latex.codecogs.com/gif.latex?4T_D) dose not end until ![](http://latex.codecogs.com/gif.latex?F_D%3D1.447). The range ![](http://latex.codecogs.com/gif.latex?1.447%3C%20F_D%3C%201.454) corresponds to period-![](http://latex.codecogs.com/gif.latex?8T_D) motion.  







# 6.Acknowledgemen and Reference  
- type the formulas with [codecogs](http://latex.codecogs.com/) and [数学公式生成器](http://www.ruanyifeng.com/webapp/formula.html) 
-[matplotlib教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)


