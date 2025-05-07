"""A 1D diffusion model"""
import numpy as np
import matplotlib.pyplot as plt


# start by setting two fixed model parameters, the diffusivity and the size of the model domain

# In[ ]:


D=100
Lx=300


# Next, set up the model grid using a NumPy array

# In[ ]:


dx=0.5
x=np.arange(start=0, stop=Lx, step=dx)
nx=len(x)


# In[ ]:


x[-7:-3]


# Set the initial conditions for the model. The cake C is a step function with a high value on the left, a low value on the right, and a step at the center of the domain.

# In[ ]:


C=np.zeros_like(x)
C_left=500
C_right=0
C[x<=Lx/2]=C_left
C[x>Lx/2]=C_right


# Plot the initial profile

# In[ ]:


plt.figure()
plt.plot(x,C,"r")
plt.xlabel("x")
plt.ylabel("C")
plt.title("Initial profile")


# Set the number of time steps of the model. Calculate a stable time step using a stability criterion.

# In[ ]:


nt=5000
dt=0.5*dx**2/D


# In[ ]:


dt


# Loop over the time steps of the model

# In[ ]:


for t in range(0, nt):
	C[1:-1] += D * dt / dx ** 2 * (C[:-2] - 2*C[1:-1] + C[2:])


# plot the result

# In[ ]:


plt.figure()
plt.plot(x,C,"r")
plt.xlabel("x")
plt.ylabel("C")
plt.title("Initial profile")

