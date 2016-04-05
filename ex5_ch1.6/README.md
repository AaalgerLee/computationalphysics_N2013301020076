# 2nd Homework for Chapter 1
## 1. Abstract

This is the 5th homework of computional physics and the 2nd homework of chapter 1. I choose *problem 1.6* as my project.

## 2. Background

The growth of population is related to the birth term as well as the death term, that is to say

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BdN%7D%7Bdt%7D%3DaN-bN%5E%7B2%7D" style="border:none;" />

the first term corresponds to the birth of new members, while the second term corresponds to deaths.

The software Mathematica gives the solution of the equation as<img src="http://chart.googleapis.com/chart?cht=tx&chl=N(t)%3D%5Cfrac%7Bace%5E%7Bat%7D%7D%7B-1%2Bbce%5E%7Bat%7D%7D" style="border:none;" />

where the constant <img src="http://chart.googleapis.com/chart?cht=tx&chl=c" style="border:none;" /> is determined by the initial value<img src="http://chart.googleapis.com/chart?cht=tx&chl=N(0)%3DN_%7B0%7D" style="border:none;" /> , that is <img src="http://chart.googleapis.com/chart?cht=tx&chl=c%3D%5Cfrac%7BN_%7B0%7D%7D%7BbN_%7B0%7D-a%7D" style="border:none;" />      
The problem requires to be solved in the following way:   
- begin by b=0 using Euler method;
- solve it with nonezero values b;
- change initial value of N and a,b to find interesting things.     
For simplicity, I set the initial population N=1unit, and the following calculation of population is based on the unit. Meanwhile, I set the unit of time as year.  
The plot can be made as a 3D one.

## 3. The main body
### 3.1. Methodology and Purpose
- Calculate with list and  for-loop in Python;
- Plot the 2D figure with matplotlib;
- Plot the 3D figure with Vpython.  
### 3.2. Coding and Calculating
The code can be found [here](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex5_ch1.6/homework1.6.py)  
### 3.3. Running and Analysis  
- 2D figure
1. For a=1,b=0 and time_interval=0.01,final_time=10
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex5_ch1.6/figure_1.png)
2. For a=1.5,b=0.1 and time_interval=0.01,final_time=10
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex5_ch1.6/figure_2.png)
3. For a=1.5,b=10 and time_interval=0.01,final_time=10
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex5_ch1.6/figure_3.png)
4. For a=1.5,b=1.5 and time_interval=0.01,final_time=10
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex5_ch1.6/figure_4png.png)
- 3D

## 4. Conclusion
- The change of population can be separated into several stages. The first stage is increase or decrease and the tendency is determined by the relative value of the constant a and b. This change is followed by the stage of stability unless b is zero.
- From the expression and the pictures above, we can see that if as time approaches infitite, the population approaches a limit, that is  <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Clim_%7Bt%5Cto%5Cinfty%7DN%3D%5Cfrac%7Ba%7D%7Bb%7D" style="border:none;" />. At this point, the mathematical expression and my calculation are compatible.  
## 5. Acknowledgement and Reference
- [Matplotlib 教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)

- [typing formula](http://www.ruanyifeng.com/webapp/formula.html)
