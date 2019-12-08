# MACHINE PROBLEM 3
# Python program that will approximate the data according to the least-norm
# error vector

# importing numpy, and math
import numpy as np
import math

# component input must be: component = np.array(([-3,174],[-2,41],[-1,4]))
def approximate(component):
    
    # Setting the coefficients of the first column of the input array to x
    x = component[:,0]
    
    # Setting the coefficients of the 2nd column of the input array to y
    y = component[:,1]
    
    # Setting the least norm to infinity 
    least=math.inf
    
    # looping for i in the degree of x from 0-10
    for i in range(0,10):
        
        # Stops the loop when i is equal to the degree of x
        if i == len(x):
            break
        
        p=np.polyfit(x,y,i)
        
        y2=np.polyval(p,x)
        
        # computing for the error vector
        error = y-y2
        
        errorvector=np.linalg.norm(error)
        
        if errorvector<least:
        
            least=errorvector
            bestfit=p
            
    print(bestfit)