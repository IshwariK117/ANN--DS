#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# 

# In[15]:


img=cv2.imread("some/wrong/path.jpg")


# In[3]:


print(img)


# In[4]:


img=cv2.imread("00-puppy.jpg")


# In[5]:


img


# In[6]:


img_bgr=cv2.imread("00-puppy.jpg")
plt.imshow(img_bgr)


# The image has been correctly loaded by openCV as a numpy array,but the color of each pixel has been sorted by BGR
# Matplotlib plot expect an RGB image so,for for a c orrect display of image ,it is necessary to swap those channels.this operation can be done either by using openCv conversion

# In[7]:


img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)


# In[8]:


img_gray=cv2.imread("00-puppy.jpg",cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray)


# In[9]:


img_gray=cv2.imread("00-puppy.jpg",cv2.IMREAD_GRAYSCALE)
plt.imshow(img_gray,cmap='gray')


# # Resize Images

# In[23]:


img_rgb.shape  
#We can see the shape , i.e., width and height and channels of the image using shape attribute.


# In[18]:


img=cv2.resize(img_rgb,(1300,275))


# In[19]:


plt.imshow(img)


# # By ratio

# In[24]:


import cv2
#assume img_rgb is already loaded with an image
w_ratio=0.5 #scaling factor for width
h_ratio=0.5 #scaling factor for height

#resize the image
new_img=cv2.resize(img_rgb,(0,0),fx=w_ratio,fy=h_ratio)

'''
cv2.resize 
this is the function from opencv library that resizes an image to a specific size
img_rgb:
This is the input image that you want to esize 
it is assumed to be in RGB format
(0,0)
this is the desired size of output image
'''


# # Flipping Image

# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


#along central x_axis
new_img=cv2.flip(new_img,0)
plt.imshow(new_img)

'''
0:
specifies how the image should flipped
   0-flipping around x-axis (verical flip)
   1-flipping around y axis (horizontal flip)
   -1 - flipping around both axes(verical and horizontal)
'''


# In[28]:


#along central y_axis
new_img=cv2.flip(new_img,1)
plt.imshow(new_img)


# In[29]:


#along central both axis
new_img=cv2.flip(new_img,-1)
plt.imshow(new_img)


# # Saving image file
# 

# In[30]:


type(new_img)


# In[31]:


cv2.imwrite('my_new_picture.jpg',new_img)


# above store in BGR format 

# # Larger display in notebook

# In[32]:


fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)
ax.imshow(new_img)


# In[ ]:




