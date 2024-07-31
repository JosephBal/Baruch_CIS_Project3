# Baruch_CIS_Project3
This was my 4th project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description

Given an integer value for K, the value for F can be determined by the following equation: 

![eqn](CodeCogsEqnF.gif)

As an example, when K = 3, F will be 2.0

Write a python program that displays the integer value of F when K = (sum of all digits of my 5 digit number).

As an example, if Jane's 5-digit number is 12345, then for Jane, K = 1+2+3+4+5 = 15, and as a result F = 610.0000000000003. Jane's program should display: 610


To get started, here is a sample program that calculates just the upper left side of the above equation and prints it out:

```python
# sample python program
from math import sqrt # this imports the sqrt function from math

K = 15
test = int((( 1 + sqrt(5) )/2) ** K)

print(test)

```
