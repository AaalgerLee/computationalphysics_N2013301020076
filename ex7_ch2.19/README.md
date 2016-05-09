Exercise 7 - trajectory of batted ball under the effect of backspin
上官俊怡 2013301020076
# 1.Abstract    
The Magnus force is taken into consideration to deal with how backspin influences the motion of a batted ball. Besides, the drag coefficient is introduced to make the model more realistic.  

# 2.Background    
Batted ball is popular among the westners, and many research has been conducted to figure out the best way to fight in the competition. There are a lot of books illustrating the motion of batted ball like The Physics of Baseball(by Robert K. Adair).  
To deal with the trajectory of a batted ball, two effects must be dealt with. One is the spin, which turns out to dominate the motion. The other concerns the drag coefficients for rough and smooth balls. In this case, we introduce the effect of spin as well as the influence of drag coefficient.  

# 3.Methodology  
The motion in three dimensions should be considered. Let x be the axis running from home plate to the pitcher, z be the horizontal direction perpendicular to x, and y be the height above the ground. We assume that the axis of rotation is parallel to y, that is, perpendicular to the ground. The equations of motion include the effects of atmospheric drag and the effects of Magnus force.  
The axis can be demonstrated as below:  
![]()插入示意图啊  

1. the atmospheric drag  
In general, air resistance can be written in the fairly innocent form  
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5Capprox-B_%7B1%7Dv-B_%7B2%7Dv%5E%7B2%7D)  
at resonable velocity, the latter term in the equation dominates for most objects.  
To make an approximation, we have  
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5Capprox-B_%7B2%7Dv%5E%7B2%7D)  
The atmospheric drag is concerned with the largest component of the velocity![](http://latex.codecogs.com/gif.latex?v_x), since the forces introduced by ![](http://latex.codecogs.com/gif.latex?v_y%2Cv_z)are much smaller：  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%20%7B%20B_%7B2%7D%20%7D%7B%20m%20%7D%20%3D0.0039&plus;%5Cfrac%7B0.0058%7D%7B1&plus;e%5E%7B%28v-v_%7Bd%7D%29/%5CDelta%7D%7D) with  
![](http://latex.codecogs.com/gif.latex?%5CDelta%3D5m/s%2Cv_%7Bd%7D%3D35m/s)  

2. the Magnus force:  
The upward component of the force on the lower half of the ball is proportional to the square of the velocity of the surface of the ball relative to the air. Besides, the downward component of the drag force on the upper half of the ball is proportional to the square of the relative velocity of that surface. So the Magnus force is equal to the difference of these two terms:  
![](http://latex.codecogs.com/gif.latex?F_M%5Cpropto%28v&plus;r%5Comega%29%5E2-%28v-r%5Comega%29%5E2%5Csim%20vr%5Comega)  
Thus the spin-dependent force can be expressed as:  
![](http://latex.codecogs.com/gif.latex?F_M%3DS_0%5Comega%20v_x)  
For the same toke,considering the angular velocoty as a vector, and we have  
![](http://latex.codecogs.com/gif.latex?%5Cvec%7BF%7D_M%3DS_0%5Cvec%7B%5Comega%7D%5Ctimes%5Cvec%7Bv%7D%3DS_0%28%5Comega_yv_z-%5Comega_zv_y%29%5Cvec%7Bx%7D&plus;S_0%28%5Comega_zv_x-%5Comega_xv_z%29%5Cvec%7By%7D&plus;S_0%28%5Comega_xv_y-%5Comega_yv_x%29%5Cvec%7Bz%7D)  
over the velocity of interest to a pitcher,50-110mph, it is estimated from the data given that  
![](http://latex.codecogs.com/gif.latex?S_0/m%5Capprox4.1%5Ctimes10%5E%7B-4%7D, where http://latex.codecogs.com/gif.latex?m%5Capprox149g)  

3. The equations of motion are then  
http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2x%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-Bvv_x&plus;%5Cfrac%7BS_0%7D%7Bm%7D%28%5Comega_yv_z-%5Comega_zv_y%29%20%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2y%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-Bvv_y&plus;%5Cfrac%7BS_0%7D%7Bm%7D%28%5Comega_zv_x-%5Comega_xv_z%29-g%20%5C%5C%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2z%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-Bvv_z&plus;%5Cfrac%7BS_0%7D%7Bm%7D%28%5Comega_xv_y-%5Comega_yv_x%29  

# 4.Code  
The code for [batted ball motion effected by spin]

# 5.Running and Analysis

# 6.Acknowledgemen and Reference  
- type the formulas with [codecogs](http://latex.codecogs.com/) in the procedure: right-click the formula, select the image attributes, copy the url in "Source" column, publish as a figure.  
- The calculation of the Magnus force is based on [The project of Feng Chen](https://www.zybuluo.com/355073677/note/339666)  
- 3d figure is based on [mplot3d tutorial](http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#scatter-plots)
