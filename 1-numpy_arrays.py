#!/usr/bin/env python
# coding: utf-8

# In[21]:


#required for image processing
import numpy as np
my_list=[0,1,2,3,4]


# In[22]:


arr=np.array(my_list)


# In[23]:


arr


# In[24]:


np.arange(0,10,2)


# In[25]:


np.ones((2,4))


# In[26]:


np.random.seed(101)
arr=np.random.randint(0,100,10)


# In[27]:


arr


# In[28]:


arr2=np.random.randint(0,100,10)


# In[29]:


arr2


# In[30]:


arr.max()


# In[31]:


arr.min()


# In[32]:


arr.mean()


# In[33]:


arr.argmin()


# In[34]:


arr


# In[35]:


arr.argmin()


# In[36]:


arr.reshape(2,5)


# Indexing

# In[37]:


mat=np.arange(0,100).reshape(10,10)


# In[38]:


mat


# In[39]:


row=0
col=1


# In[40]:


mat[row,col]


# In[41]:


mat[:,col]


# In[42]:


mat[row,:]


# In[43]:


mat[0:3,0:3]


# In[ ]:





# In[ ]:





# In[ ]:




