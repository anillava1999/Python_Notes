## Convert radians into degrees ##

import math

No_degree = int(input("Enter the number of degree "))

def Radi_Degree(value):
    Result = No_degree * 180/math.pi
    print(Result)

Radi_Degree(No_degree)
