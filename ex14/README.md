Exercise 14--- Waves on a String and Its Frequency Spectrum. Problem 6.6 + 6.12 + 6.16  
2013301020076 上官俊怡  

# 1. Abstract
Here the particular case of waves on a string is considered. At the beginning, a solution for the wave equation in the ideal case is introduced and developed, that is, for a perfectly flexible and frictionless string. Only one initial Gaussian wave packet and two initial Gaussian wave packets are considered to show that the wave packets are unaffected by the collisions. Besides, Fourier analysis is applied in the spectral analysis to exam the waves on a string.  

# 2. Background


# 3. Methodology and Solutions
## 3.1 Numerical Solution to the Waves in the Ideal Case
The central equation of wave motion is  
![]( http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20y%7D%7B%5Cpartial%20t%5E2%7D%3Dc%5E2%5Cfrac%7B%5Cpartial%5E2%20y%7D%7B%5Cpartial%20x%5E2%7D) where ![]( http://latex.codecogs.com/gif.latex?c%5E2%3D%5Cfrac%7BT%7D%7B%5Crho%20%7D) is the ratio of the tension in the string to the density per length.  
To solve the time-dependent solution ![]( http://latex.codecogs.com/gif.latex?y%28x%2Ct%29), the wave equation should be attacked with rather different numerical treatments than those employed in the work with Laplace’s equation. The numerical approach can be written as follows.  
The variables are treated as discrete ones as ![]( http://latex.codecogs.com/gif.latex?x%3Di%5CDelta%20x%2Ct%3Dn%5CDelta%20t).  
The displacement of the string is a function of i and n, that is, ![]( http://latex.codecogs.com/gif.latex?y%28i%2Cn%29%5Cequiv%20y%28x%3Di%5CDelta%20x%2Ct%3Dn%5CDelta%20t%29).  
Inserting the expression for the second partial derivative, the wave equation can be rewritten as  
![]( http://latex.codecogs.com/gif.latex?%5Cfrac%7By%28i%2Cn&plus;1%29&plus;y%28i%2Cn-1%29-2y%28i%2Cn%29%7D%7B%28%5CDelta%20t%29%5E2%7D%5Capprox%20c%5E2%5B%5Cfrac%7By%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29-2y%28i%2Cn%29%7D%7B%28%5CDelta%20x%29%5E2%7D%5D)  
Rearranging the above equation, we have  
![]( http://latex.codecogs.com/gif.latex?y%28i%2Cn&plus;1%29%3D2%281-r%5E2%29y%28i%2Cn%29-y%28i%2Cn-1%29&plus;r%5E2%5By%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29%5D)  
Where ![]( http://latex.codecogs.com/gif.latex?r%5Cequiv%20c%5CDelta%20t/%5CDelta%20x). Thus if we know the string configuration as time steps n and n-1, the configuration at step n+1 can be calculated.
The boundary condition is ![]( http://latex.codecogs.com/gif.latex?y%280%2Cn%29%3Dy%28M%2Cn%29%5Cequiv%200) and the initial condition is ![]( http://latex.codecogs.com/gif.latex?y%28i%2C0%29%3Dy_o%28i%29).  

## 3.2 Routine Propagate for Simulating Waves on a String
+ Set the parameter combination ![]( http://latex.codecogs.com/gif.latex?r%5Cequiv%20c%5CDelta%20t/%5CDelta%20x).  
+ Loop through the interior points ![]( http://latex.codecogs.com/gif.latex?i%3D1) through ![]( http://latex.codecogs.com/gif.latex?i%3DM-1). Update according to  
> ![]( http://latex.codecogs.com/gif.latex?y%28i%2Cn&plus;1%29%3D2%281-r%5E2%29y%28i%2Cn%29-y%28i%2Cn-1%29&plus;r%5E2%5By%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29%5D)  
+ The ends at ![]( http://latex.codecogs.com/gif.latex?i%3D0) and ![]( http://latex.codecogs.com/gif.latex?i%3DM) are fixed as zero for all time steps.  

## 3.3 Power Spectrum
If we are interested in the frequencies ad relative amplitudes of the Fourier components but do not care about their phases, power spectrum is a useful way to display the results of an FFT.  
Formally, the power spectrum of a function ![]( http://latex.codecogs.com/gif.latex?y%28t%29) can be defined as the Fourier transformation of its autocorrelation  
![]( http://latex.codecogs.com/gif.latex?Corr%5By%5D%28t%29%3D%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Dy%28t%29%5E%5Cast%20y%28t&plus;%5Ctau%29d%5Ctau)  
And the power spectrum is given by  
![]( http://latex.codecogs.com/gif.latex?PS%5By%5D%28f%29%3D%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7Dy%28t%29%5E%5Cast%20y%28t&plus;%5Ctau%29e%5E%7B2%5Cpi%20if%5Ctau%7Dd%5Ctau%3D%5Cleft%20%7C%20Y%28f%29%20%5Cright%20%7C%5E2)  


# 4. Code
Code for [Displacement of Waves on An Ideal String]  
Code for [Frequency Spectrum of Waves on a String]  

# 5. Running and Analysis
## 5.1  Displacement of Waves on An Ideal String
If the initial wave packet is ![](http://latex.codecogs.com/gif.latex?y_0%28x%29%3De%5E%7B-1000%5Ctimes%28x-0.3%29%5E2%7D), the result is:  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex14/figure_1.png)  
动图1号  

If the initial wave packet is ![](http://latex.codecogs.com/gif.latex?y_0%28x%29%3D-2e%5E%7B-300%5Ctimes%28x-0.6%29%5E2%7D), the result is:  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_2.png)  
动图2号  

If the initial wave packet is ![](http://latex.codecogs.com/gif.latex?y_0%28x%29%3De%5E%7B-1000%5Ctimes%28x-0.3%29%5E2%7D-2e%5E%7B-300%5Ctimes%28x-0.6%29%5E2%7D), the result is:  
![](https://github.com/JunyiShangguan/computationalphysics_N2013301020076/blob/master/ex13/figure_3.png)  
动图3号

From the results above, we can draw the conclusion that when there are two Gaussian wave packets located at different places on the string, the wave packets may then propagate and collide but the wave packets are unaffected by the collisions.  

## 5.2Frequency Spectrum of Waves on a String






# 6. Acknowledgement and Reference
- codecogs(http://latex.codecogs.com/)  
- Computational Physics, Nicholas J. Giordano & Hisao Nakanishi  
- Matplotlib Tutorial(http://www.labri.fr/perso/nrougier/teaching/matplotlib/)
- [FFT演示程序](http://old.sebug.net/paper/books/scipydoc/fft_study.html)  
