#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


# TO USE X AND Y LIST WE CAN MAKE A GRAPH AND SHOW THE GRAPH TO USE SHOW() FUNCTION 
x=[0,1,2,3,4,5]
y=[0,2,4,6,8,10]
# here we changed the size of graph
plt.figure(figsize=(5,4), dpi=50)

# here we changed the diagonal line on the graph and its style
# we can also shot hand character for attributes so it wont take more spaces(check it on documentation)
plt.plot(x,y, color='blue',marker='.',linestyle='--',linewidth=2,label ='2x',markersize=15)

#here we used title function to give graph name and we can also change its font qnd also change font size
plt.title('First Graph!',fontdict={'fontname':'Comic Sans MS','fontsize': 22})

#here we use xlabel and ylabel to give name of yaxis and xaxis
plt.xlabel('X-AXIS',fontdict={'fontname':'Comic Sans MS','fontsize': 16})
plt.ylabel('Y-AXIS', fontdict={'fontname':'Comic Sans MS','fontsize': 16})

#here we will use Matplotlib with Numpy
#we have given the dashed line after it cross the line
a=np.arange(0,5,0.5)
plt.plot(a[:4],a[:4]**2,'r',label='x-2')
plt.plot(a[2:],a[2:]**2,'r--',label='x-2')

# we can also use xticks and yticks for gap between line
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10,12,14])

plt.legend()

plt.show()


# In[3]:


# Use Function of Numpy to plot value on Graph
a=np.arange(0,5,0.5)
plt.plot(a,a**3)
plt.show()


# In[4]:


days = [1,2,3,4,5,6,7,8,9,10]
tempreture = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,]
plt.figure(figsize=(5,5),dpi=50)
plt.plot(days,tempreture, color='blue',linestyle='--',marker='.' )
plt.grid(color='black')
plt.show()


# In[5]:


i=[0,1,2,3,4,5]
j=[0,2,4,6,8,10]
plt.plot(i,j,'ro')
plt.title('DOT GRAPH')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()


# In[6]:


Programming_Languages=['Python','Java','C','C++','PHP']
Students=[20,45,34,65,46]
plt.bar(Programming_Languages,Students,color='r')
plt.title('Students Using Languages',fontdict={'fontsize':20})
plt.xlabel('Programming_Languages')
plt.ylabel('Students')
plt.show()


# In[7]:


Programming_Languages=['Python','Java','C','C++','PHP']
Students=[20,45,34,65,46]
plt.barh(Programming_Languages,Students,color='r')
plt.title('Students Using Languages',fontdict={'fontsize':20})
plt.xlabel('Programming_Languages')
plt.ylabel('Students')
plt.show()


# In[8]:


Langs=['Python','Java','C','C++','PHP']
Students=[20,45,34,65,46]
plt.figure(figsize=(5,5),dpi=70)
plt.pie(Students, labels = Langs,autopct='%1.2f%%')
plt.title('Students Using Languages',fontdict={'fontsize':20})
plt.xlabel('Programming_Languages')
plt.ylabel('Students')
plt.show()


# In[9]:


Langs=['Python','Java','C','C++','PHP']
Students=[20,45,34,65,46]
plt.scatter(Langs,Students)
plt.show()


# In[10]:


import matplotlib.image as mpimg


# In[11]:


img=mpimg.imread('photo1.jpg')


# In[12]:


plt.imsave('photo2.jpg', img, cmap='gray', origin='lower')


# In[13]:


plt.imshow(img)
plt.show()


# In[ ]:




