Exercise 10 – the Lorentz model ex 3.26/3.29/3.31
上官俊怡 2013301020076
# 1.Abstract    
In this report, the Lorentz model is applied to grasp a basic understanding of fluid mechanics, especially Rayleigh-Benard problem. Besides, phase-space plot, Poincare section are investigated.  

# 2.Background    
Lorentz was studying the basic equations of fluid mechanics, which are known as the Navier-Stokes equations and which can be regarded as Newton’s law written in a form appropriate to a fluid. The specific situation he considered was the Rayleigh-Benard problem, which concerns a fluide in a container whose top and bottom surfaces are held at different temperatures. Indeed, he grossly simplified the problem as he reached to the so-called Lorentz equations, or equivalently, the Lorentz model, which provided a major contribution to the modern field of physics.  

# 3.Methodology and Solution
**The Lorentz equations (the Lorentz model)**  
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5C%5C%5Cfrac%7Bdx%7D%7Bdt%7D%3D%5Csigma%20(y-x)%0A%5C%5C%5Cfrac%7Bdy%7D%7Bdt%7D%3D-xz%2Brx-y%0A%5C%5C%5Cfrac%7Bdz%7D%7Bdt%7D%3Dxy-bz" style="border:none;" />  
The Lorentz variables <img src="http://chart.googleapis.com/chart?cht=tx&chl=x%2C%20y%2C%20z" style="border:none;" /> are derived from the temperature, density and velocity variables in the original Navier-Stokes equations, and the parameters <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Csigma%20%2C%20r%2C%20b" style="border:none;" /> are measures of the temperature difference across the fluid and other fluid parameters. 

**Euler Method**  
Euler-Cromer method is designed for second-order differential equations, so it is not directly applicable to the Lorentz model.  
Here, the Euler algorithm can actually be used to treat the Lorentz problem. 

**Parameters in the Lorentz Model**  
There are three parameters in the Lorentz equations <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Csigma%2Cb%2Cr" style="border:none;" />, and the behavior one finds depends on their values.  
In this report, the custom is followed and <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Csigma%3D10%2Cb%3D8%2F3" style="border:none;" /> is used. The parameter <img src="http://chart.googleapis.com/chart?cht=tx&chl=r" style="border:none;" /> is a measure of the temperature difference between the top and the bottom of the fluid. In fact, <img src="http://chart.googleapis.com/chart?cht=tx&chl=r" style="border:none;" /> plays the role analogous to the drive amplitude.

# 4.Code  

# 5.Running and Analysis

# 6.Acknowledgemen and Reference  
-  [数学公式生成器] ( http://www.ruanyifeng.com/webapp/formula.html)  
