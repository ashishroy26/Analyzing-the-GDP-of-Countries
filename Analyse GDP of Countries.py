#!/usr/bin/env python
# coding: utf-8

# Analyzing the GDP of Countries-
# 
# Tasks-
# 
# 1)Find and print the name of the country with the highest GDP
# 
# 2)Find and print the name of the country with the lowest GDP
# 
# 3)Print out text and input values iteratively
# 
# 4)Print out the entire list of the countries with their GDPs
# 
# 5)Print the highest GDP value, lowest GDP value, mean GDP value, standardized GDP value, and the sum of all the GDPs
# 
# 

# In[2]:


import numpy as np


# In[16]:



Countries=np.array(['Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh','Belarus','Belgium','Bhutan','Brazil','Bulgaria','Cambodia','Cameroon','Chile','China','Colombia','Cyprus','Denmark','El Salvador','Estonia','Ethiopia','Fiji','Finland','France','Georgia','Ghana','Grenada','Guinea','Haiti','Honduras','Hungary','India','Indonesia','Ireland','Italy','Japan','Kenya', 'South Korea','Liberia','Malaysia','Mexico', 'Morocco','Nepal','New Zealand','Norway','Pakistan', 'Peru','Qatar','Russia','Singapore','South Africa','Spain','Sweden','Switzerland','Thailand', 'United Arab Emirates','United Kingdom','United States','Uruguay','Venezuela','Vietnam','Zimbabwe'])



GDP_per_capita = np.array([55.225482,629.9553062,11601.63022,25306.82494,27266.40335,19466.99052,588.3691778,2890.345675,24733.62696,1445.760002,4803.398244,2618.876037,590.4521124,665.7982328,7122.938458,2639.54156,3362.4656,15378.16704,30860.12808,2579.115607,6525.541272,229.6769525,2242.689259,27570.4852,23016.84778,1334.646773,402.6953275,6047.200797,394.1156638,385.5793827,1414.072488,5745.981529,837.7464011,1206.991065,27715.52837,18937.24998,39578.07441,478.2194906,16684.21278,279.2204061,5345.213415,6288.25324,1908.304416,274.8728621,14646.42094,40034.85063,672.1547506,3359.517402,36152.66676,3054.727742,33529.83052,3825.093781,15428.32098,33630.24604,39170.41371,2699.123242,21058.43643,28272.40661,37691.02733,9581.05659,5671.912202,757.4009286,347.7456605])


# In[4]:


Countries, GDP_per_capita


# In[5]:


print(max(GDP_per_capita))


# In[6]:


max_gdp_per_capita=GDP_per_capita.argmax()
max_gdp_per_capita


# ## The name of the country with the highest GDP

# In[7]:


highest_gdp_country=Countries[max_gdp_per_capita]


# In[8]:


highest_gdp_country


# In[9]:


print("Country with the highest GDP is",highest_gdp_country)


# ## The name of the country with the lowest GDP

# In[10]:


lowest_gdp=GDP_per_capita.argmin()
lowest_gdp


# In[11]:


lowest_gdp_country=Countries[lowest_gdp]
lowest_gdp_country


# In[12]:


print("Country with lowest GDP is",lowest_gdp_country)


# In[18]:


for country in Countries:
   print(format(country))  #Printing out text and input values iteratively


# Printing out the entire list of the countries with their GDPs

# In[24]:


for i in range(len(Countries)):
    country = Countries[i]
    country_gdp_per_capita = GDP_per_capita[i]
    print("Country {} per capita GDP is {}".format(country, country_gdp_per_capita))


# Printing the highest GDP value, lowest GDP value, mean GDP value, standardized GDP value, and the sum of all the GDPs
# 

# In[29]:


print("Highest GDP value is ",GDP_per_capita.max())
print("Lowest GDP value is ",GDP_per_capita.min())
print("Mean GDP value is ",GDP_per_capita.mean())
print("Standardized GDP value is ",GDP_per_capita.std())
print("Sum of all the GDP's is ",GDP_per_capita.sum())


# In[ ]:




