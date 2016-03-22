


> Written with [StackEdit](https://stackedit.io/).
#homework for chapter 1
##abstract
For the homework of the 1st chapter of computational  physics, I choose *problem 1.4* as my project.

##background
- There are two particles involved in the decay, ie, nuclei A and B. And B nuclei is the decay product of nuclei A.
- The number of each nuclei is governed by the following differential equations:
\begin{eqnarray*}
\ \frac{dN_B}{dt}&=& \frac{N_A}{\tau_A} -\frac{N_B}{\tau_B}\\
\frac{dN_A}{dt}&=& -\frac{N_A}{\tau_A}
\end{eqnarray*}

 In the above equations$N_A$and$N_B$represent the number of nuclei A and B respectively. $\tau_A$and $\tau_B$are the decay time constants for each type of nucleus.

##the main body
### 1. methodology and purpose
- Mathematically, Euler method is a possible one to solve differential equation.
- Technically in Python, the notion of array and  for-loop can be used for calculation.
- Matplotlib is utilized to depict the data.
### 2.procedure

``` flow

st=>start: Start
e=>end
assi=>operation: Assign parameters
op=>operation: Calculation
cond=>condition: Within final_time?
print=>operation: Print time and number of nucleus
fig=>operation: Figure

st->assi->op->cond
cond(yes)->op
cond(no)->print->fig->e
```
### 3.coding


### 4.running and analysis







##conclusion





##acknowledgement and reference
- [Matplotlib 教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)