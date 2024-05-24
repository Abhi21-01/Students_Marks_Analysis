#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv(r"C:\Users\singa\Downloads\archive (2)\Expanded_data_with_more_features.csv")


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


df.drop(columns = 'Unnamed: 0', inplace = True)


# In[14]:


df


# In[10]:


df.drop_duplicates(inplace = True)


# In[11]:


df


# In[16]:


df.dropna(subset=['NrSiblings'], inplace = True)
df['NrSiblings'] = df['NrSiblings'].astype('int64')


# In[22]:


df.info()


# In[25]:


ax = sns.countplot(x='Gender', data =df)
ax.bar_label(ax.containers[0])

plt.show()


# ##### From the above analysis, we can clearly see that number of female students are more than the number of male students. 

# In[27]:


parent_edu = df.groupby('ParentEduc').agg({'MathScore': 'mean', 'ReadingScore': 'mean', 'WritingScore': 'mean'})
parent_edu


# In[35]:


sns.heatmap(parent_edu, annot= True)
plt.title('Relationship b/w Parent Education and Student Score')
plt.show()


# ##### From the above chart analysis, it is clear that the parent's education has direct impact on their child's performance. 

# In[30]:


parent_marriage_status = df.groupby('ParentMaritalStatus').agg({'MathScore': 'mean', 'ReadingScore': 'mean', 'WritingScore': 'mean'})
parent_marriage_status


# In[34]:


sns.heatmap(parent_marriage_status, annot= True)
plt.title('Relationship b/w Parent Marital Status and Student Score')
plt.show()


# ##### From the above analysis, it is clear that Parents Marital Status has no impact on their child's score 

# In[37]:


sns.boxplot(x= 'MathScore', data = df)
plt.show()


# In[38]:


sns.boxplot(x= 'ReadingScore', data = df)
plt.show()


# In[39]:


sns.boxplot(x= 'WritingScore', data = df)
plt.show()


# In[46]:


ethnic_groupA = df[(df['EthnicGroup'] == 'group A')].count()
ethnic_groupB = df[(df['EthnicGroup'] == 'group B')].count()
ethnic_groupC = df[(df['EthnicGroup'] == 'group C')].count()
ethnic_groupD = df[(df['EthnicGroup'] == 'group D')].count()
ethnic_groupE = df[(df['EthnicGroup'] == 'group E')].count()

l = ['groupA', 'groupB', 'groupC', 'groupD', 'groupE']
mlist = [ethnic_groupA['EthnicGroup'], ethnic_groupB['EthnicGroup'], ethnic_groupC['EthnicGroup'], ethnic_groupD['EthnicGroup'], ethnic_groupE['EthnicGroup'], ]
plt.pie(mlist, labels = l, autopct = '%1.2f%%')
plt.title('Distribution of Ethnic Groups')
plt.show()


# In[50]:


ax = sns.countplot(x = 'EthnicGroup', data = df)
ax.bar_label(ax.containers[0])
plt.show()


# In[ ]:




