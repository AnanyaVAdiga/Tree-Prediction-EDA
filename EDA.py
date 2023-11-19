#!/usr/bin/env python
# coding: utf-8

# # Data Import and Overview
# 
# 
# 

# ## Dataset Loading

# In[4]:


import numpy as np #numerical computations
import pandas as pd # data processing
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


# ## Basic Overview

# In[6]:


# df means DaraFrame
df = pd.read_csv('Tree_Data.csv') # Reading the CSV file into a DataFrame
print ("Data is loaded!")


# In[49]:


df.shape


# In[7]:


df.head() # to display the first 5 rows of the DataFrame


# In[8]:


df.tail() #   to display the last 5 rows of the DataFrame


# In[8]:


# unique values in each column
df.nunique()


# # Data Description

# ## Summary Statistics

# In[27]:


df.describe() # gives the basic descriptive statistics for each column


# ## Data Types

# In[47]:


df.info()# check null and dtypes


# ### Exploring Data

# In[41]:


# define numerical and categorical columns
numeric_features = [feature for feature in df.columns if df[feature].dtype != 'object']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'object']

# print columns
print('we have {} numerical features: {}'.format(len(numeric_features),numeric_features ))
print('we have {} categorical features: {}'.format(len(categorical_features),categorical_features ))


# # Feature Information

# ##### No: Seedling unique ID number.
# #### Plot: Number of the field plot the seedling was planted in. (1-18)
# #### Subplot: Subplot within the main plot the seedling was planted in. Broken into 5 subplots (1 per corner, plus 1 in the middle). (A-E)
# #### Species: Includes Acer saccharum, Prunus serotina, Quercus alba, and Quercus rubra.
# ##### Light ISF: Light level quantified with HemiView software. Represents the amount of light reaching each subplot at a height of 1m.
# #### Light Cat: Categorical light level created by splitting the range of Light_ISF values into three bins (low, med, high).
# #### Core: Year the soil core was removed from the field.
# #### Soil: Species from which the soil core was taken. Includes all species, plus Acer rubrum, Populus grandidentata, and a sterilized  conspecific for each species.
# #### Adult: Individual tree that soil was taken from. Up to 6 adults per species. Used as a random effect in analyses.
# #### Sterile: Whether the soil was sterilized or not.
# #### Conspecific: Whether the soil was conspecific, heterospecific, or sterilized conspecific.
# #### Myco: Mycorrhizal type of the seedling species (AMF or EMF).
# #### SoilMyco: Mycorrhizal type of the species culturing the soil (AMF or EMF).
# #### PlantDate: The date that seedlings were planted in the field pots.
# #### AMF: Percent arbuscular mycorrhizal fungi colonization on the fine roots of harvested seedlings.
# #### EMF: Percent ectomycorrhizal fungi colonization on the root tips of harvested seedlings.
# #### Phenolics: Calculated as nmol Gallic acid equivalents per mg dry extract (see manuscript for detailed methods)
# #### NSC: Calculated as percent dry mass nonstructural carbohydrates (see manuscript for detailed methods)
# #### Lignin: Calculated as percent dry mass lignin (see manuscript for detailed methods)
# #### Census: The census number at which time the seedling died or was harvested.
# ### Time: The number of days at which time the seedling died or was harvested.
# #### Event: Used for survival analysis to indicate status of each individual seedling at a given time (above)
# 0 = harvested or experiment ended
# 1 = dead
# #### Harvest: Indicates whether the seedling was harvested for trait measurement.
# #### Alive: Indicates if the seedling was alive at the end of the second growing season. "X" in this field indicates alive status.
# 

# ### Distribution of Numerical Features

# In[56]:


# Histograms of numerical columns
numeric_features = df.select_dtypes(include='number').columns
for col in numeric_features:
    plt.hist(df[col])
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {col}')
    plt.show()


# ### Distributions of Categorical Features

# In[57]:


# Bar plots for categorical columns
categorical_features = df.select_dtypes(exclude='number').columns
for col in categorical_features:
    sns.countplot(x=col, data= df)
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)
    plt.show()


# # Missing Values and Data Cleaning

# ## Missing Values Handling¶

# In[58]:


# Missing value count for each column
df.isnull().sum()


# In[59]:


df


# ## Data Cleaning

# In[60]:


df['Alive'] = df['Alive'].replace('X', 1)
df['Harvest'] = df['Harvest'].replace('X', 1)

label = LabelEncoder()
for column in df.columns:
    df[column] = label.fit_transform(df[column])


# In[61]:


df


# # Explratory Data Analysis

# ## Univariate Analysis

# ###### The term univariate analysis refers to the analysis of one variable prefix "uni" means "one".
# ###### The purpose of univariate analysis is to understand the distribution of values for a single variable.

# ### Numerical Features

# In[62]:


numeric_features = df.select_dtypes(include='number').columns
for col in numeric_features:
    plt.figure(figsize=(5,3))
    sns.histplot(df[col], kde=True)
    plt.title(f'Univariate Analysis of Numerical Features of {col}')
    plt.show()


# ## Correlation Matrix 

# In[12]:


# Correlation matrix
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()


# ## Target Variable Analysis

# In[60]:


# Target variable distribution
sns.countplot(x='Alive', data=df)
plt.title('Distribution of Target Variable')
plt.show()


# ### Identifying the Outliers

# In[42]:


# Boxplot to identify outliers
for col in numerical_cols:
    sns.boxplot(df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()




# In[ ]:





# In[ ]:





# In[ ]:




