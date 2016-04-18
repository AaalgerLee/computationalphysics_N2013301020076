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
- For trajectory project:
: Euler method can be applied to the situations mentioned above to depict to trajectory.  
- For the firing system:
: waiting to be considered ???É¨ÃèÊÇÊ²Ã´  

## 3.2Code  
Here is the code for [trajectory project]  
Here is the code for [firing system]   
## 3.3Running and Analysis  
### The trajectory project  
### The firing system  
# 4.Conclusion  
# 5.Acknowledegment and Reference  
- [Python使用matplotlib绘制动画的方法](http://www.jb51.net/article/66441.htm)
- [typing formula](http://www.ruanyifeng.com/webapp/formula.html)
- []
