#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('C:\Users\500221324\Downloads\archive\supermarket_sales - Sheet1.csv')
df.head()


# In[29]:


df


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df = df.drop(['Invoice ID', 'Date', 'Time'], axis = 1)


# In[8]:


df.head(5)


# In[9]:


print(df.shape)
df['Gender'].value_counts()


# In[10]:


sns.countplot('Gender' , data = df)


# In[11]:


gender_dummies  = pd.get_dummies(df['Gender'])
gender_dummies.head()


# In[13]:


df = pd.concat([df, gender_dummies], axis = 1)
df.head()


# In[14]:


plt.figure(figsize = (12,6))
sns.barplot(x = 'Product line', y = 'Female', data = df)


# In[15]:


plt.figure(figsize = (12,6))
sns.barplot(x = 'Product line', y = 'Male', data = df)


# In[16]:


place_df = pd.DataFrame(df['City'].value_counts())
place_df


# In[17]:


sns.barplot(x = place_df.index  , y = place_df['City'], palette = 'hot')


# In[18]:


payment_df = pd.DataFrame(df['Payment'].value_counts())
payment_df 


# In[27]:


sns.barplot(x =payment_df.index , y = payment_df.Payment)


# In[28]:


plt.figure(figsize= (12,6))
sns.barplot(x = df['Product line'], y = df['gross income'])


# In[30]:


xdata = [0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,6))
sns.barplot(y = df['Product line'], x = df['Rating'])
plt.xticks(xdata)


# In[31]:


plt.figure(figsize = (12,6))
sns.barplot(x = df['Total'] , y = df['Product line'])


# In[32]:


xdata = [1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,6))
sns.distplot(df['Quantity'])
plt.xticks(xdata)


# In[33]:


quantity_df = pd.DataFrame(df['Quantity'].value_counts())
quantity_df


# In[35]:


plt.figure(figsize=(12,6))
sns.barplot(x = quantity_df.index , y = quantity_df['Quantity'] , palette = 'inferno')


# In[36]:


sns.heatmap(df.corr())






