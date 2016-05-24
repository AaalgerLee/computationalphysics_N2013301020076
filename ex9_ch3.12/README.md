Exercise 9 - chaos in the nonlinear, damped, driven pendulum(ex3.12/16/21)  
上官俊怡 2013301020076  
# 1.Abstract    
In this report, a physical pendulum is discussed. An external driving force, dissipation and nonlinearity are applied at the same time. Besides, Poincare section, attractor and bifurcation diagram are investigated to grasp a better undestanding of the movement of pendulum and the notation of chaos.  

# 2.Background    
- **Physicsl pendulum**: we add an external driving force, dissipation and nonlinearity to the pendulum at the same time rather than discuss these ingredients separately. First, we do not assume the small-angle approximation and thus do not expand ![](http://latex.codecogs.com/gif.latex?sin%5Ctheta)term in equation. second, friction of the form ![](http://latex.codecogs.com/gif.latex?-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%20t%7D) and sinusoidal driving force ![](http://latex.codecogs.com/gif.latex?F_Dsin%28%5COmega_Dt%29) are introduced. From this procedure, we are supposed to see: (1)it is possible for a system to be both deterministic and unpredictable and this is what the term chaos means;(2)the behavior in the chaotic regime is not completely random, but can be describe by a strange attractorin phase space.  
- **Chaos**: the system to be both deterministic and unpredictable. That is, a system can oey certain determnistic laws physics, but stil exhibit behavior that is unpredictable du to an extreme sensitivity to initial conditions.  
- **Poincare section**: in the phase-space graph, plot![](http://latex.codecogs.com/gif.latex?%5Comega)versus![](http://latex.codecogs.com/gif.latex?%5Ctheta)only at times that are in phase with the driving force. That is, only the points with ![](http://latex.codecogs.com/gif.latex?%5COmega_Dt%3D2n%5Cpi) are displayed where n is an integer. Ihis is known as Poincare section. And it is a very useful way to plot and analyze the behavior of a dynamical system.  
- **Attractor**:the trajectory of pendulum is drawn to the surface, which is known as attractor. Chaotic attractors have a frictal structure and are usually reffered to as strange attractors.  
- **Bifurcation diagram**: it is a nice way to predict how the trasition from nonchaos to chaos comes about. It can be constructed in the following manner. Calculate ![](http://latex.codecogs.com/gif.latex?%5Ctheta)as a function of time, wait for 300driving periods so that the initial transients have decayed away, plot![](http://latex.codecogs.com/gif.latex?%5Ctheta) at times that were in phase with the driving forcr as a function of ![](http://latex.codecogs.com/gif.latex?F_D) to 400th drive periods. And repeat the process for various ![](http://latex.codecogs.com/gif.latex?F_D) and show the result in a figure, which is known as bifurcation diagram.  


# 3.Methodology and Solution
## 3.1 Physical Model 
Putting the ingredients together, the model is called a nonlinear, damped, driven pendulum, the physical pendulum. The equation of motion is:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_Dsin%28%5COmega_Dt%29)  
The above ordinary differential equation has no known exact solution.  
Thenatural frequency of undamped pendulum is ![](http://latex.codecogs.com/gif.latex?%5COmega%3D%5Csqrt%7Bg/l%7D)  

## 3.2 Numerical Method
- **The equation of motion**  
It can be rewritten as two first-order differential equations as follows:  
![](http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5Comega%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Comega&plus;F_Dsin%28%5COmega_Dt%29%20%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Comega)  

- **Euler-Cromer Method**  
In this project, Euler-Cromer method is applied. Refer to the Appendix of the textbook, it can be deduced that:  
![](http://latex.codecogs.com/gif.latex?%5C%5C%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;f%28%5Ctheta_i%2C%5Comega_i%2Ct_i%29%5CDelta%20t%20%5C%5C%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t%20%5C%5Ct_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t)  
where ![](http://latex.codecogs.com/gif.latex?f%28%5Ctheta%2C%5Comega%2Ct%29%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Comega&plus;F_Dsin%28%5COmega_Dt%29)  

- **Adjust theta**  
The value of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) is adjusted so as to keep it in the range between ![](http://latex.codecogs.com/gif.latex?%5B%5Cpi%2C-%5Cpi%5D). Now the pendulum is free to swing all the way around its pivot point, and values of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) differed by ![](http://latex.codecogs.com/gif.latex?2%5Cpi) correspond to the same position. So this adjustment is done because for ploting purpose it is convenient to keep ![](http://latex.codecogs.com/gif.latex?%5Ctheta) in the range.  

# 4.Code  
Here is the code for[theta V.S.t & Phase-space Plot](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/ex9.1.py)  
Here is the code for[poincare section](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/ex9.2.py)

# 5.Running and Analysis
## 5.1 The Influence of ![](http://latex.codecogs.com/gif.latex?F_D)
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_1.png)  
The above figure is the behavior of the driven, damped, nonlinear pendulum in 60 seconds whose parameters are set as![](http://latex.codecogs.com/gif.latex?%5Comega%28t%3D0%29%3D0%2C%20%5Ctheta%28t%3D0%29%3D0.2%2C%20q%3D0.5%2Cl%3D9.8%2C%20%5COmega_D%3D0.66)with![](http://latex.codecogs.com/gif.latex?dt%3D0.04seconds). The left figure is the behavior of ![](http://latex.codecogs.com/gif.latex?%5Ctheta)as a function of time while the right is the behavior of ![](http://latex.codecogs.com/gif.latex?%5Comega).  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_1.3.png)  
This is the behavior of![](http://latex.codecogs.com/gif.latex?%5Ctheta)under![](http://latex.codecogs.com/gif.latex?F_D%3D1.2), with and without the resetting of the angle. The pendulum does not settle into any sort of repeating steady-state behavior, at least in the range shown here.  
From the figures above, it is obvious that at low driven force, the pendulum experiences simple harmonic oscillation. But at high drive, the motion is chaotic.  
## 5.2 Phase-space Plot
In this part, the trajectory ofangular velocity ![](http://latex.codecogs.com/gif.latex?%5Comega) as a function of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) is demonstrated.  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_2.png)  
This is the results for![](http://latex.codecogs.com/gif.latex?%5Comega) as a function of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) for a pendulum in 500 seconds. The parameters are the same as in Fig 1.1 and Fig 1.2. The figure on the right is for high drive, and the "jump" is the result of the adjustment of ![](http://latex.codecogs.com/gif.latex?%5Ctheta).  
树上63页解释分析

![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex9_ch3.12/figure_3.png)





# 6.Acknowledgemen and Reference  
- type the formulas with [codecogs](http://latex.codecogs.com/)  
-[matplotlib教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)


