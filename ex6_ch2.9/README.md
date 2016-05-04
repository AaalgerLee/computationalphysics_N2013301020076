Exercise 6--trajectory of the cannon shell  
上官俊怡2013301020076
# 1.Abstrack  
This is the 6th exercise of computional physics. The project is about the design of cannon trajectory while taking the air resistence into consideration. In addition, the firing system is also designed.  
# 2.Background
- Newton's second law can be applied as   
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt_%7B2%7D%7D%3Da_%7Bx%7D%3D%5Cfrac%7BF_%7Bx%7D%7D%7Bm%7D%3D%5Cfrac%7BF_%7Bdrag%2Cx%7D%7D%7Bm%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt_%7B2%7D%7D%3Da_%7By%7D%3D%5Cfrac%7BF_%7By%7D%7D%7Bm%7D%3D-g%2B%5Cfrac%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D" style="border:none;" />  

- For the trajectory project, the following conditions should be  applied:   

1. No air drag    
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=F_%7Bdrag%2Cx%7D%3DF_%7Bdrag%2Cy%7D%3D0" style="border:none;" />  

2. Air drag is only related to the velocity     
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BF_%7Bdrag%7D%7D%7Bm%7D%3D-Bv%5E%7B2%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=F_%7Bdrag%2Cx%7D%3D-mBvv_%7Bx%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=F_%7Bdrag%2Cy%7D%3D-mBvv_%7By%7D" style="border:none;" />  

3. Air drag is related to air density under isothermal approximation: treat the atmosphere as an ideal gas with constant temperature  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=F_%7Bdrag%7D%3D-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_%7B0%7D%7DmBv%5E%7B2%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Crho%20%3D%5Crho_%7B0%7De%5E%7B-mgy%2Fk_%7BB%7DT%7D%3D%20%5Crho_%7B0%7De%5E%7B-y%2Fy_%7B0%7D%7D" style="border:none;" />  

4. Air drag is related to air density under adiabatic approximation: assume that air is a poor heat conductorand that convection is very slow.  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=F_%7Bdrag%7D%3D-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_%7B0%7D%7DmBv%5E%7B2%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Crho%20%3D%5Crho_%7B0%7D(1-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D)%5E%7B%5Calpha%20%7D" style="border:none;" />

- For the firing system:  
 ???      

# 3.The Main Body    
## 3.1Method  
For trajectory project:  
Euler method can be applied to the situations mentioned above to depict to trajectory.  

1. No air drag: the second order equations describing the movement can be re written as first order ones. To use the Euler methon, we can write each derivative in finite form, which leads to the following equations:  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=x_%7Bi%2B1%7D%3Dx_%7Bi%7D%2Bv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7Bx%2Ci%2B1%7D%3Dv_%7Bx%2Ci%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=y_%7Bi%2B1%7D%3Dy_%7Bi%7D%2Bv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7By%2Ci%2B1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t" style="border:none;" />  

2. Air drag is only related to speed:for the same reason, we can deduce that  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=x_%7Bi%2B1%7D%3Dx_%7Bi%7D%2Bv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7Bx%2Ci%2B1%7D%3Dv_%7Bx%2Ci%7D-Bvv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=y_%7Bi%2B1%7D%3Dy_%7Bi%7D%2Bv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7By%2Ci%2B1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-Bvv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  

3. Isothermal approximation:  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=x_%7Bi%2B1%7D%3Dx_%7Bi%7D%2Bv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7Bx%2Ci%2B1%7D%3Dv_%7Bx%2Ci%7D-Be%5E%7B-y_%7Bi%7D%2Fy_%7B0%7D%7Dvv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=y_%7Bi%2B1%7D%3Dy_%7Bi%7D%2Bv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7By%2Ci%2B1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-Be%5E%7B-y_%7Bi%7D%2Fy_%7B0%7D%7Dvv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  

4. Adiabatic approximation:  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=x_%7Bi%2B1%7D%3Dx_%7Bi%7D%2Bv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7Bx%2Ci%2B1%7D%3Dv_%7Bx%2Ci%7D-B(1-%5Cfrac%7Bay_%7Bi%7D%7D%7BT_%7B0%7D%7D)%5E%7B%5Calpha%20%7Dvv_%7Bx%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=y_%7Bi%2B1%7D%3Dy_%7Bi%7D%2Bv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=v_%7By%2Ci%2B1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-B(1-%5Cfrac%7Bay_%7Bi%7D%7D%7BT_%7B0%7D%7D)%5E%7B%5Calpha%20%7Dvv_%7By%2Ci%7D%5CDelta%20t" style="border:none;" />  

- For the firing system:  
???  

## 3.2Code  
Here is the code for [no-drag case](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/trajectory1.py)  
Here is the code for [with-air-drag case](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/trajectory2.py)  
Here is the code for [with density correction]()  
Here is the code for [firing system]   
## 3.3Running and Analysis  
### The trajectory project  
- For the case with no air resistence, we set the initial velocity as 700m/s.
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/no_drag.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/table1-nodrag.PNG)  
When the angle equals 45,the range is the maximum. Meanwhile, as the angle increases, the time it takes for the cannon to hit the target on the ground is longer.

- For the case with air resistence only related to speed:  
We set the constant <img src="http://chart.googleapis.com/chart?cht=tx&chl=B%3D4%5Ctimes%2010%5E%7B-5%7D%2Fm" style="border:none;" /> and the initial velocity equals to 700m/s as well.  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/withdrag.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/table2-airdrag.PNG)  
When air resistance is involved as above,the maximum range occurs at a lower firing angle. For the parameters we have used here, the largest range is obtained with a firing angle approximately 40. This is accord with our intuition that the longest range is obtained by shooting low into the wind.  
From the air-density-independent cases above, we can see that air resistance plays a major role in the firing problem. However, there is another piece of physics that we should have taken into consideration. From the pictures above, we can see that the shell travels at high altitude, where the air density will be lower than that at the sea level. Therefore, we should investigate how the air density varies with altitude. This brings statistical and thermal physics of the atmosphere into what had been a kinematic problem as follows.  
- For the isothermal case  
We can set the constant<img src="http://chart.googleapis.com/chart?cht=tx&chl=y_%7B0%7D%3Dk_%7BB%7DT%2Fmg%5Capprox%201.0%5Ctimes%2010%5E%7B4%7Dm" style="border:none;" />  

- For the adiabatic case   
The parameter <img src="http://chart.googleapis.com/chart?cht=tx&chl=a%5Capprox%206.5%5Ctimes%2010%5E%7B-3%7DK%2Fm" style="border:none;" /> fits the mearesured data fairly well. And the exponent <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha%20%5Capprox%202.5" style="border:none;" />for air. Besides, for simplicity, we choose the temperature <img src="http://chart.googleapis.com/chart?cht=tx&chl=T_%7B0%7D%3D300K" style="border:none;" />

For simplicity, we do the density-correction canses together. Here is the result:
![]()

Compared with the constant density canse, it is obvious that the density correction can incerase the distance the cannon shell tralvells.

### The firing system  
# 4.Conclusion  
# 5.Acknowledegment and Reference  
- [Python使用matplotlib绘制动画的方法](http://www.jb51.net/article/66441.htm)
- [typing formula](http://www.ruanyifeng.com/webapp/formula.html)
- []
