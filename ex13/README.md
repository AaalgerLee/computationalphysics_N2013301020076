Exercise 12--- Electric Potential and Field under Laplace's Equation
Problem 5.3 + 5.7 + 5.16  
2013301020076 上官俊怡  

# 1. Abstract
The capacitor problem is investigated and its symmetry property is made use of. Besides, this project is done by the Jacobi relaxation method, the Gauss-Seidel method and Simultaneous Over-Relaxation (SOR) method.  

# 2. Background
In regions with no source of electric charge, the electric potential obeys the so-called Laplace's equation:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20z%5E2%7D%3D0)  
Different from the differential equations that are given initial conditions and that can be solved by Euler method or Runge-Kutta method, Laplace's equation is often introduced with boundary conditions, which specify the value on some surface in the space. Alternatively, the boundary conditions might be given in terms of the electric field, which is proportional to the gradient of electric potential.  
Thus, the relaxation method is introduced to solve the project. It is convenient for dealing with the class of partial differential equations known as ellipitic equations, of which Laplace's equation is one example.  
问题背景是树上140页点5.6图

# 3. Methodology and Solutions
## 3.1 Equations That May Need
Electric potential satisfies the Laplace's equation:  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20z%5E2%7D%3D0)  
Electric field can be calculated by differentiating the potential:  
![](http://latex.codecogs.com/gif.latex?%5Coverrightarrow%7BE%7D%3D-%5Cbigtriangledown%20V)  
or equivalently, ![](http://latex.codecogs.com/gif.latex?E_i%3D-%5Cfrac%7B%5Cpartial%20V%7D%7B%5Cpartial%20x_i%7D) where ![](http://latex.codecogs.com/gif.latex?i) corresponds to ![](http://latex.codecogs.com/gif.latex?x%2Cy%2Cz).  
To be more specific, we have  
![](http://latex.codecogs.com/gif.latex?E_x%3D-%5Cfrac%7B%5Cpartial%20V%7D%7B%5Cpartial%20x%7D%5Capprox%20%5Cfrac%7BV%28i&plus;1%2Cj%29-V%28i-1%2Cj%29%7D%7B2%5CDelta%20x%7D)  

## 3.2 Analytical approximation
Points in the regime are specified by integers ![](http://latex.codecogs.com/gif.latex?i%2Cj%2Ck) with ![](http://latex.codecogs.com/gif.latex?x%3Di%5CDelta%20x%2Cy%3Dj%5CDelta%20y%2Cz%3Dk%5CDelta%20z). The goal is to determine the potential ![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%2Ck%29%5Cequiv%20V%28i%5CDelta%20x%2Cj%5CDelta%20y%2Ck%5CDelta%20z%29) on each site of the lattice.  
Because we have  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20V%7D%7B%5Cpartial%20x%7D%5Capprox%20%5Cfrac%7BV%28i&plus;1%2Cj%2Ck%29-V%28i%2Cj%2Ck%29%7D%7B%5CDelta%20x%7D)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20V%7D%7B%5Cpartial%20x%7D%5Capprox%20%5Cfrac%7BV%28i%2Cj%2Ck%29-V%28i-1%2Cj%2Ck%29%7D%7B%5CDelta%20x%7D)  
we can deduce that  
![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D%20%26%5Capprox%20%5Cfrac%7B1%7D%7B%5CDelta%20x%7D%5B%5Cfrac%7B%5Cpartial%20V%7D%7B%5Cpartial%20x%7D%28i&plus;%5Cfrac%7B1%7D%7B2%7D%29-%5Cfrac%7B%5Cpartial%20V%7D%7B%5Cpartial%20x%7D%28i-%5Cfrac%7B1%7D%7B2%7D%29%5D%20%5C%5C%20%26%5Capprox%5Cfrac%7B1%7D%7B%5CDelta%20x%7D%5B%5Cfrac%7BV%28i&plus;1%2Cj%2Ck%29-V%28i%2Cj%2Ck%29%7D%7B%5CDelta%20x%7D-%5Cfrac%7BV%28i%2Cj%2Ck%29-V%28i-1%2Cj%2Ck%29%7D%7B%5CDelta%20x%7D%5D%20%5C%5C%20%26%5Capprox%20%5Cfrac%7BV%28i&plus;1%2Cj%2Ck%29&plus;V%28i-1%2Cj%2Ck%29-2V%28i%2Cj%2Ck%29%7D%7B%28%5CDelta%20x%29%5E2%7D%20%5Cend%7Balign*%7D)  
Repeat the process on the direction of ![](http://latex.codecogs.com/gif.latex?y%2Cz), and insert them into the Laplace's equation, we have  
![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Balign*%7D%20V%28i%2Cj%2Ck%29%20%3D%26%5Cfrac%7B1%7D%7B6%7D%5BV%28i&plus;1%2Cj%2Ck%29&plus;V%28i-1%2Cj%2Ck%29&plus;V%28i%2Cj&plus;1%2Ck%29%5C%5C%20%26&plus;V%28i%2Cj-1%2Ck%29&plus;V%28i%2Cj%2Ck&plus;1%29&plus;V%28i%2Cj%2Ck-1%29%5D%20%5Cend%7Balign*%7D)  
where the denominator corresponds to twice the dimension of interest.  
 
## 3.3 Jacobi Relaxation Method
Jacobi relaxation method can be manipulated in the following procedures:  
initialize-V: set suitable initial values for ![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%2Ck%29).  
Update-V: use the values in ![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%2Ck%29) to compute an improved eatimate for ![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%2Ck%29). This can be operated twice to eliminate the need to swap the values between old and new arrays.  

> Take a two-dimension case as an example.  
> + Let ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V) be the total cumulative change in ![](http://latex.codecogs.com/gif.latex?V) during this update loop and set the initial value as ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V%3D0).  
> + Loop through all points ![](http://latex.codecogs.com/gif.latex?%28i%2Cj%29) in the lattice except the boundary, where the values of ![](http://latex.codecogs.com/gif.latex?V_n) are fixed by the boundary conditions.  
>  ![](http://latex.codecogs.com/gif.latex?V_%7Bn&plus;1%7D%28i%2Cj%29%20%3D%5Cfrac%7B1%7D%7B4%7D%5BV_n%28i&plus;1%2Cj%29&plus;V_n%28i-1%2Cj%29&plus;V_n%28i%2Cj&plus;1%29&plus;V_n%28i%2Cj-1%29%5D)  
>  Add ![](http://latex.codecogs.com/gif.latex?%5Cleft%20%7C%20V_n%28i%2Cj%29-V_%7Bn&plus;1%7D%28i%2Cj%29%20%5Cright%20%7C) to ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V)  
> + Return ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V) and ![](http://latex.codecogs.com/gif.latex?V_%7Bn&plus;1%7D) to the calling program.  

Laplace-calculate: takes care of calling update-V and testing for convergence  
The convergence limit is concerned with ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V). > The average deviation between the two consequent calculated potential should be much smaller than the value of 1 per site. Thus, it is recommended that a appropriate limit is ![](http://latex.codecogs.com/gif.latex?%5CDelta%20V%5Cleqslant%201%5Ctimes%2010%5E%7B-5%7D%5Ctimes%20N) where ![](http://latex.codecogs.com/gif.latex?N) is the number of sites.  

## 3.4  The Gauss-Seidel Method
 The Gauss-Seidel method differs in that it uses the new values as they become available. The order in which they become available depends on how the lattice is looped through. That is  
![](http://latex.codecogs.com/gif.latex?V_%7Bnew%7D%28i%2Cj%29%20%3D%5Cfrac%7B1%7D%7B4%7D%5BV_%7Bold%7D%28i&plus;1%2Cj%29&plus;V_%7Bnew%7D%28i-1%2Cj%29&plus;V_%7Bold%7D%28i%2Cj&plus;1%29&plus;V_%7Bnew%7D%28i%2Cj-1%29%5D)  
The bonus of this method is that the potential can be stored in one array in the calculation.

## 3.5  Simultaneous Over-Relaxation (SOR) Method
The slow convergence can be overcomed by SOR method. Let ![](http://latex.codecogs.com/gif.latex?V%5E*%28i%2Cj%29) be the new value of potential calculated from the Gauss-Seidel method. We can then think of  
![](http://latex.codecogs.com/gif.latex?%5CDelta%20V%28i%2Cj%29%5Cequiv%20V%5E*%28i%2Cj%29-V_%7Bold%7D%28i%2Cj%29)  
as the change recommended by the Gauss-Seidel algorithm. To speed up the convenience, the potential can be changed by a larger amount according to  
![](http://latex.codecogs.com/gif.latex?V_%7Bnew%7D%28i%2Cj%29%3D%5Calpha%5CDelta%20V%28i%2Cj%29&plus;V_%7Bold%7D%28i%2Cj%29)  
where the factor ![](http://latex.codecogs.com/gif.latex?%5Calpha) measures how much we “over-relax”. For a problem on a two-dimensional square grid, the best choice for ![](http://latex.codecogs.com/gif.latex?%5Calpha) is  
![](http://latex.codecogs.com/gif.latex?%5Calpha%5Capprox%20%5Cfrac%7B2%7D%7B1&plus;%5Cpi/L%7D)  


# 4. Code
The code for [Jacobi Relaxation Method](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/13.1.Jacobi.py)  
The code for [Gauss-Seidel Method](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/13.2.GS.py)  

# 5. Running and Analysis
## 5.1 Jacobi Relaxation Method
When ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.1), the results are as follows:  
The number to iterate is 67  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_1.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_2.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_3.png)  

When ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.05), the results are as follows:  
The number to iterate is 217  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_4.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_5.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_6.png)  
It can be induced that when ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.1) is changed to ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.05), the number of iteration increases from 67 to 217, almost four times it used to be.  

## 5.2 Gauss-Seidel Relaxation Method
When ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.1), the results are as follows:  
The number to iterate is 57  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_7.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_8.png)  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_9.png)  

When ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.1) is changed to ![](http://latex.codecogs.com/gif.latex?%5CDelta%3D0.05), the number of iteration increases from 57 to 188, also almost four times it used to be.  
Thus, the number of iteration satisfies <img src="http://chart.googleapis.com/chart?cht=tx&chl=N_%7Biter%7D%5Csim%20L%5E2" style="border:none;" />  

# 6. Acknowledgement and Reference
- [codecogs](http://latex.codecogs.com/)
- Computational Physics, Nicholas J. Giordano & Hisao Nakanishi
- [Matplotlib Tutorial](http://www.labri.fr/perso/nrougier/teaching/matplotlib/)







