#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[2]:


mss = np.load('mss.npy')
mss_shape = np.shape(mss)
#Original image
plt.imshow(mss,'gray')
plt.show()


# In[23]:


#Channel parameters
x0 = [0.2050078785,0.7949921215]
x1 = [0.7316819956,0.2683180044]


# In[8]:


#Converting mss to a string
MSS = ''
for i in range(mss_shape[0]):
    for j in range(mss_shape[1]):
        MSS += str(mss[i][j])


# In[9]:


#definition for encoding for every two single bit
def encoder(a):
    if(a == '00'):
        return '00000'
    if(a == '01'):
        return '00111'
    if(a == '10'):
        return '11100'
    if(a == '11'):
        return '11011'


# In[11]:


#encoding
mss_enc = ''
for i in range(int(len(MSS)/2)):
    start = i*2
    end = (i+1)*2
    mss_enc += encoder(MSS[start:end])


# In[12]:


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


# In[13]:


#Simulating the channel
Y = ''
for i in range(len(mss_enc)):
    Y += channel(mss_enc[i],x0,x1)


# In[51]:


#ML decoder for a every five bits
def decoder(a,x0,x1):
    cw = ['00000','00111','11100','11011']
    m = None
    index = 0
    for j in cw:
        index +=1
        temp = 1
        for i in range(len(a)):
            k = j[i]
            i = a[i]
            if(k == '0'):
                if(i == '0'):
                    temp = temp*x0[0]
                if(i == '1'):
                    temp = temp*x0[1]
            if(k == '1'):
                if(i == '0'):
                    temp = temp*x1[0]
                if(i == '1'):
                    temp = temp*x1[1]
        if(m == None or temp > m):
            m = temp
            b = index
    if(b == 1):
        return '00'
    if(b == 2):
        return '01'
    if(b == 3):
        return '10'
    if(b == 4):
        return '11'


# In[47]:


#decoding the recieved bits
X = ''
for i in range(int(len(Y)/5)):
    start = i*5
    end = (i+1)*5
    X += decoder(Y[start:end],x0,x1)


# In[48]:


#Converting string back to an array
X_arr = np.zeros(len(X))
for i in range(len(X)):
    X_arr[i] = int(X[i])


# In[49]:


#bit error rate
X_arr = X_arr.reshape(400,300)
bit_error_rate = np.sum(np.abs(X_arr-mss))/(300*400)
print(bit_error_rate)


# In[50]:


#Image constructed from decoded bits
plt.imshow(X_arr,'gray')
plt.show()


# In[ ]:




