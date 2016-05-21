Exercise 9 - chaos in the nonlinear, damped, driven pendulum(ex3.12/16/21)  
上官俊怡 2013301020076  
# 1.Abstract    
In this report, a physical pendulum is discussed. An external driving force, dissipation and nonlinearity are applied at the same time. And Poincare section is investigated.  

# 2.Background    
We add an external driving force, dissipation and nonlinearity to the pendulum at the same time rather than discuss these ingredients separately. First, we do not assume the small-angle approximation and thus do not expand ![](http://latex.codecogs.com/gif.latex?sin%5Ctheta)term in equation. second, friction of the form ![](http://latex.codecogs.com/gif.latex?-q%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%20t%7D) and sinusoidal driving force ![](http://latex.codecogs.com/gif.latex?F_Dsin%28%5COmega_Dt%29) are introduced.  

# 3.Methodology and Solution
## 3.1 Physical Model 
Putting the ingredients together, the model is called a nonlinear, damped, driven pendulum, the physical pendulum. The equation of motion is:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D&plus;F_Dsin%28%5COmega_Dt%29)  
The above ordinary differential equation has no known exact solution.  

## 3.2 Numerical Method
- The equation of motion can be rewritten as two first-order differential equations as follows:  
![](http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5Comega%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Comega&plus;F_Dsin%28%5COmega_Dt%29%20%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Comega)  

- Second-Order Runge-Kutta Method  
In this project, second-order Runge-Kutta method is applied. Refer to the Appendix of the textbook, it can be deduced that:  
![](http://latex.codecogs.com/gif.latex?%5C%5C%5Ctheta%27%3D%5Ctheta_i&plus;%5Cfrac%7B1%7D%7B2%7D%5Comega_i%5CDelta%20t%20%5C%5C%5Comega%27%3D%5Comega_i&plus;%5Cfrac%7B1%7D%7B2%7Df%28%5Ctheta_i%2C%5Comega_i%2Ct_i%29%5CDelta%20t%20%5C%5Ct%27%3Dt_i&plus;%5Cfrac%7B1%7D%7B2%7D%5CDelta%20t%20%5C%5C%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;f%28%5Ctheta%27%2C%5Comega%27%2Ct%27%29%5CDelta%20t%20%5C%5C%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega%27%5CDelta%20t%20%5C%5Ct_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t)  
where ![](http://latex.codecogs.com/gif.latex?f%28%5Ctheta%2C%5Comega%2Ct%29%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta-q%5Comega&plus;F_Dsin%28%5COmega_Dt%29)  


# 4.Code  

# 5.Running and Analysis

# 6.Acknowledgemen and Reference  
- type the formulas with [codecogs](http://latex.codecogs.com/)  
