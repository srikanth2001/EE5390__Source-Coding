#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
from matplotlib import pyplot as plt


# In[20]:


mss = np.load('mss.npy')
mss_shape = np.shape(mss)
#Original image
plt.imshow(mss,'gray')
plt.show()


# In[21]:


#Channel parameters
x0 = [0.2050078785,0.7949921215]
x1 = [0.7316819956,0.2683180044]


# In[22]:


#Converting mss to a string
MSS = ''
for i in range(mss_shape[0]):
    for j in range(mss_shape[1]):
        MSS += str(mss[i][j])


# In[23]:


#definition for encoding for a single bit
def encoder(a):
    if(a == '0'):
        return '000'
    if(a == '1'):
        return '111'


# In[24]:


#encoding
mss_enc = ''
for i in range(len(MSS)):
    mss_enc += encoder(MSS[i])


# In[25]:


#definition for simulating channel for a single bit
def channel(a,x0,x1):
    if(a == '0'):
        temp = np.random.uniform(0,1)
        if(temp < x0[0]):
            return '0'
        else:
            return '1'
    if(a == '1'):
        temp = np.random.uniform(0,1)
        if(temp < x1[0]):
            return '0'
        else:
            return '1'


# In[26]:


#Simulating the channel
Y = ''
for i in range(len(mss_enc)):
    Y += channel(mss_enc[i],x0,x1)


# In[27]:


#ML decoder for a every three bits
def decoder(a,x0,x1):
    temp1 = 1
    temp2 = 1
    for i in a:
        if(i == '0'):
            temp1 = temp1*x0[0]
            temp2 = temp2*x1[0]
        if(i == '1'):
            temp1 = temp1*x0[1]
            temp2 = temp2*x1[1]
    if(temp1 > temp2):
        return '0'
    else:
        return '1'


# In[32]:


#decoding the recieved bits
X = ''
for i in range(int(len(Y)/3)):
    start = i*3
    end = (i+1)*3
    X += decoder(Y[start:end],x0,x1)


# In[42]:


#Converting string back to an array
X_arr = np.zeros(len(X))
for i in range(len(X)):
    X_arr[i] = int(X[i])


# In[48]:


#bit error rate
X_arr = X_arr.reshape(400,300)
bit_error_rate = np.sum(np.abs(X_arr-mss))/(300*400)
print(bit_error_rate)


# In[49]:


#Image constructed from decoded bits
plt.imshow(X_arr,'gray')
plt.show()


# In[ ]:




