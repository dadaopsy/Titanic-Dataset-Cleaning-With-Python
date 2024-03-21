#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[77]:


df=pd.read_excel('titanic Data.xlsx')


# In[78]:


df


# In[79]:


df.info()


# In[80]:


df.head(2)


# In[81]:


df.describe()


# VISUAL ASSESSMENT
# -change 1,2,3 to first, second and third class respectively in the pclass column.
# -seperate the last name from the other names.
# -check why the age column is a float and check for the null rows.
# -delete the ticket column.
# 
# -PROGRAMMATIC ASSESSMENT
# -replace the null row in the Age column.
# -delete the Cabin column (it has alot of null rows)
# -change pclass column to string.

# In[82]:


df['Pclass']=df['Pclass'].replace([1,2,3],['First Class','Second Class','Third Class'])


# In[23]:


df


# In[83]:


df['Embarked']=df['Embarked'].replace(['S','C','Q'],['Southampton','Cherbourg','Queenstown'])


# In[27]:


df


# In[84]:


df['Survived']=df['Survived'].replace([0,1],['Dead','Survived'])


# In[85]:


df


# In[86]:


df[['Last_Name', 'Prefix_OtherNames']]=df['Name'].str.split(',', expand=True)


# In[87]:


df


# In[88]:


df=df.drop(columns=['Name', 'Ticket', 'Cabin'])


# In[89]:


df


# In[90]:


df['Age'].fillna(0, inplace=True)


# In[91]:


df.info()


# In[92]:


columns = df.columns.tolist()


# In[93]:


columns.remove('Last_Name')
columns.remove('Prefix_OtherNames')


# In[94]:


columns.insert(1, 'Last_Name')
columns.insert(2, 'Prefix_OtherNames')


# In[95]:


df = df[columns]


# In[96]:


df


# In[97]:


df.info()


# In[99]:


df.dropna(subset=['Embarked'], inplace=True)


# In[100]:


df.info()


# In[101]:


df


# In[ ]:




