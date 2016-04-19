Exercise 6--trajectory of the cannon shell  
上官俊怡2013301020076
# 1.Abstrack  
This is the 6th exercise of computional physics. The project is about the design of cannon trajectory while taking the air resistence into consideration. In addition, the firing system is also designed.  
# 2.Background
- Newton's second law can be applied as   
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3D%5Cfrac%7BF_%7Bx%7D%7D%7Bm%7D%3Da_%7Bx%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3D%5Cfrac%7BF_%7By%7D%7D%7Bm%7D%3Da_%7By%7D" style="border:none;" />  

- For the trajectory project, the following conditions should be  applied:   

1. No air drag    
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=F_%7Bdrag%7D%3D-mBv%5E%7B2%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=f_%7Bx%7D%3D0" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=f_%7By%7D%3D-mg" style="border:none;" />   

2. Air drag is only related to the velocity     
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3Da_%7Bx%7D%3D-Bvv_%7Bx%7D" style="border:none;" />  
> <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3Da_%7By%7D%3Dg-Bvv_%7By%7D" style="border:none;" />  

3. Air drag is related to its density-isothermal  

4. Air drag is related to its density-adiabatic  

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

3. Isothermal case:
4. Adiabatic case:
- For the firing system:  
???  

## 3.2Code  
Here is the code for [no-drag case](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/trajectory1.py)  
Here is the code for [with-air-drag case](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/trajectory2.py)  
Here is the code for [isothermal case]()  
Here is the code for [adiabatic case]()  
Here is the code for [firing system]   
## 3.3Running and Analysis  
### The trajectory project  
- For the case with no air resistence
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/no_drag.png)  

- For the case with air resistence only related to speed  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex6_ch2.9/withdrag.png)  

- For the isothermal case

- For the adiabatic case 
### The firing system  
# 4.Conclusion  
# 5.Acknowledegment and Reference  
- [Python使用matplotlib绘制动画的方法](http://www.jb51.net/article/66441.htm)
- [typing formula](http://www.ruanyifeng.com/webapp/formula.html)
- []
