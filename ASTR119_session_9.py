
# coding: utf-8

# # A Newton-Raphson Root Finding Implementation

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# ### Define the function for root finding

# In[16]:


def function_for_root(x):
    a = 1.01
    b = -3.04
    c = 2.07
    return a*x**2 + b*x + c


# ### Define the function's derivative

# In[17]:


def derivative_for_root(x):
    a = 1.01
    b = -3.04
    return 2*a*x + b


# In[18]:


### Define the primary work function


# In[19]:


def newton_raphson_root_finding(f, dfdx, x_start, tol):
    flag = 1
    imax = 10000
    i=0
    x_old = x_start
    x_new = 0.0
    y_new = 0.0


# In[25]:


def newton_raphson_root_finding(f, dfdx, x_start, tol):
    flag = 1
    imax = 10000
    i=0
    x_old = x_start
    x_new = 0.0
    y_new = 0.0 
    while(flag):
    
        x_new = x_old - f(x_old)/dfdx(x_old)
    
        print(x_new, x_old, f(x_old), dfdx(x_old))
    
        y_new = f(x_new)
        if(np.fabs(y_new)<tol):
            flag = 0
        else:
            x_old = x_new
            i += 1
        if(i>=imax):
            printf("Max iterations reached.")
            raise StopIteration('Stopping iterations after '.i)
    return x_new

x_start = 0.5
tolerance = 1.0e-6

print(x_start, function_for_root(x_start))

x_root = newton_raphson_root_finding(function_for_root, derivative_for_root, x_start, tolerance)
y_root = function_for_root(x_root)

s = "Root found with y(%f) = %f" % (x_root, y_root)
print(s)

