from numpy import exp, cos, linspace
import os, time, glob
from math import sqrt

def compute(u,t,a):
    """Return filename of plot of the damped_vibration function."""
    s=(u*t)+((a*t*t)/2)
    return s
   
if __name__ == '__main__':
    print (compute(1, 1, 1))

def compute2(u,a,t):
    """Return filename of plot of the damped_vibration function."""
    v=u+(a*t)
    return v
   
if __name__ == '__main__':
    print (compute2(1, 0.1, 1))  

def compute3(q,t):
    """Return filename of plot of the damped_vibration function."""
    i=(q/t)
    return i
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute3(1,1))    

def compute4(u,a,s):
    """Return filename of plot of the damped_vibration function."""
    v=sqrt((u*u)+(2*a*s))
    return v
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute4(1, 1, 1))

def compute5(m,r):
    """Make constant of G as 6.67408*10^-11"""
    v=sqrt(2*6.67408*(10**-11)*float(m/r))
    return v
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute5(1,1))

def compute6(m,a):
    """Return filename of plot of the damped_vibration function."""
    f=m*a
    return f
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute6(1,1))    

def compute7(m1,m2,r):
    """Return filename of plot of the damped_vibration function."""
    G=6.67408*(10**-(11))
    f=(G*float(m1*m2/(r**2)))
    return f
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute7(1,1,1))

def compute8(m,r):
    """Return filename of plot of the damped_vibration function."""
    G=6.67408*(10**-(11))
    g=(G*float(m/(r**2)))
    return g
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute8(1,1))

def compute9(m, v):
    """Return filename of plot of the damped_vibration function."""
    e=float(m)*float(v*v)/2
    return e
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    
if __name__ == '__main__':
    print (compute9(1,1))    

def compute10(m,h):
    """Return filename of plot of the damped_vibration function."""
    e=9.8*float(m*h)
    return e
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    

if __name__ == '__main__':
    print (compute10(1,1))    

