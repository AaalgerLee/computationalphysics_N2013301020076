


> Written with [StackEdit](https://stackedit.io/).

#Homework for Chapter 1

上官俊怡2013301020076
## 1. Abstract
For the homework of the 1st chapter of computational  physics, I choose *problem 1.4* as my project.

## 2. Background
- There are two particles involved in the decay, ie, nuclei A and B. And B nuclei is the decay product of nuclei A.
- The number of each nuclei is governed by the following differential equations:
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BdN_%7BA%7D%7D%7Bdt%7D%3D-%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20_%7BA%7D%7D" style="border:none;" /> and <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BdN_%7BB%7D%7D%7Bdt%7D%3D%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20_%7BA%7D%7D-%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20_%7BB%7D%7D" style="border:none;" />

 In the above equations <img src="http://chart.googleapis.com/chart?cht=tx&chl=N_%7BA%7D" style="border:none;" /> and <img src="http://chart.googleapis.com/chart?cht=tx&chl=N_%7BB%7D" style="border:none;" /> represent the number of nuclei A and B respectively. <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctau%20_%7BA%7D" style="border:none;" /> and <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctau%20_%7BB%7D" style="border:none;" /> are the decay time constants for each type of nucleus.

## 3. The main body
### 3.1. Methodology and Purpose
- Mathematically, Euler method is a possible one to solve differential equation.
- Technically in Python, the notion of array and  for-loop can be used for calculation.
- Matplotlib is utilized to depict the data.
- Beautify the plot.
- Check with the graph of mathematical results.

### 3.2. Procedure
- Begin by assigning values to each parameters. And we choose the decay constant of A as a constant, namely, tau_A=1s
- Caculate until the final time;
- Draw a figure indicating the number of each nuclei.
- Compare the figure with the mathematical result.

### 3.3. Coding and Calculating
- Mathematically, the equations can be solved as
<img src="http://chart.googleapis.com/chart?cht=tx&chl=N_%7BA%7D%3DA_%7B0%7De%5E%7B-t%2F%5Ctau%20_%7BA%7D%7D" style="border:none;" />
<img src="http://chart.googleapis.com/chart?cht=tx&chl=N_%7BB%7D%3D%5Cfrac%7B%5Ctau%20_%7BB%7D%7D%7B%5Ctau%20_%7BA%7D-%5Ctau%20_%7BB%7D%7DA_%7B0%7De%5E%7B-t%2F%5Ctau%20_%7BA%7D%7D%2B(B_%7B0%7D-%5Cfrac%7B%5Ctau%20_%7BB%7D%7D%7B%5Ctau%20_%7BA%7D-%5Ctau%20_%7BB%7D%7DA_%7B0%7D)%5Ccdot%20e%5E%7B-t%2F%5Ctau%20_%7BB%7D%7D" style="border:none;" />
- For simplicity, we set<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctau%20_%7BA%7D%3D1%20second" style="border:none;" />. And the initial number of A is 100.
The code can be found [here](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex4_ch1.4/ex4_ch1.4.py)

### 3.4. Running and Analysis
1. We can set<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctau%20_%7BB%7D%3D0.5%2Ctimeinterval%3D0.01s%2Cfinaltime%3D10s" style="border:none;" /> 

- When the initial numbers satisfy<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BN_%7BA0%7D%7D%7B%5Ctau%20_%7BA%7D%7D-%5Cfrac%7BN_%7BB0%7D%7D%7B%5Ctau%20_%7BB%7D%7D%3E0" style="border:none;" />, suppose <img src="http://chart.googleapis.com/chart?cht=tx&chl=N_B%3D30" style="border:none;" />

The result is
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex4_ch1.4/figure_1.png)

The number of B witnesses an increase and a decrease, while the number of A keeps falling.
Compared with the figure of mathematical solution, the fit is quite well. 


- When the initial numbers satisfy <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BN_%7BA0%7D%7D%7B%5Ctau%20_%7BA%7D%7D-%5Cfrac%7BN_%7BB0%7D%7D%7B%5Ctau%20_%7BB%7D%7D%3C0" style="border:none;" />, suppose <img src="http://chart.googleapis.com/chart?cht=tx&chl=N_%7BB0%7D%3D70" style="border:none;" />

The result is 
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex4_ch1.4/figure_2.png)

The number of both nuclei decrease.
Compared with the figure of mathematical solution, the fit is quite well. 

2. If we change time_interval,while keep <img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Ctau%20_%7BB%7D%3D0.5%2Cfinaltime%3D10%2Cinitial%20number%20of%20B%3D30" style="border:none;" />

- if time_interval=0.1
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex4_ch1.4/figure_3.png)

- if time_interval=0.5
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex4_ch1.4/figure_4.png)

In the figures above, the dotted curved are plotted from the mathematical solution of the dacey functions.
Thus,we can deduce that the smaller time_interval is, the better our figure is fitted. 

## 4. Conclusion
The ratio of the decay constants influences the curve.

The value of time_interval influences the accuracy of the calcuation.

Anyway, the two curves are approaching some limit.

## 5. Acknowledgement and Reference
- [Matplotlib 教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)

- [typing formula](http://www.ruanyifeng.com/webapp/formula.html)
