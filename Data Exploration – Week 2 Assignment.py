#!/usr/bin/env python
# coding: utf-8

# ## Data Exploration 
# In this Jupyter Notebook, I am importing and exploring a dataset titled CalEnviroSceen 3.0. This data helps identify California communities that are most affected by many sources of pollution, and where people are often especially vulnerable to pollution’s effects. When conducting data exploration, I will comment on my steps and preliminary findings, using commands learned in class.

# In[15]:


import pandas as pd 
import geopandas as gpd


# ### Explanation #1
# Below, I am importing the dataset CalEnviroScreen 3.0 using geopandas and creating the variable 'calenviroscreen'.

# In[19]:


# Import dataset CalEnviroScreen 3.0
calenviroscreen = gpd.read_file('ces3results.csv')


# ### Explanation #2
# Below, I am using the 'type' command to give me an output showing the type of dataframe I am working with.

# In[20]:


# what's the data type?
type(calenviroscreen)


# #### Output #1
# This is spatial data, as reflected by the GeoDataFrame.

# ### Explanation #3
# Below, I use the .head() command to show me the first five rows of the data frame and thus see what the data look like.

# In[21]:


# what does the data look like?
calenviroscreen.head()


# #### Output #2
# This shows the first five rows of the data frame 'calenviroscreen'.

# ### Explanation #4
# Below, I use the .info() command to present more detailed information about the data.

# In[25]:


# use .info() to learn more about the data
calenviroscreen.info()


# #### Output #3
# This gives the data type, how many records there are in the data frame (8035), there are 6 columns (as noted by the 0-5). For most columns, there aree values in every siingle row. Most datatypes are 'object', which is the most general type of pandas dtype and is assigned to the column if the column has mixed types.

# ### Explanation #5
# Below, I use the command '.shape' to learn more about what is in my data, such as how many rows are there? What are the columns? How many rows represent a particular slice of data?

# In[28]:


# how many rows and columns?
calenviroscreen.shape


# #### Output #4
# This gives me two nuggets of data: 8035 is the number of rows, and there are 6 columns.

# ### Explanation #6
# Below, I use the command  .columns.to_list() to show the names of the columns in a list format.

# In[31]:


# use command .columns.to_list() to show the names of the columns in a list format.
calenviroscreen.columns.to_list()


# #### Output #5
# The output of this operation gave me the names of the columns (Census Tract','Total Population','California County', 'ZIP','Nearby City', and 'geometry') and presented them as a list.

# ### Explanation #7
# Below, I use the .value_counts() argument to give me the number of data points for each Califorrnia County

# In[33]:


# Use .value_counts() to ....
calenviroscreen['California County'].value_counts()


# #### Output #6
# This operation gives me the name of each county and it correlating integer next to it as the data type.

# ### Explanation #8
# Below, I save the above operation's result as a variable 'county_count' to be able to do more with it in the future such as plot it or create a bar chart.

# In[47]:


# save it as a variable
county_count = calenviroscreen['California County'].value_counts()
county_count


# #### Output #7
# The output of the operation looks the same as the previous operation, but it is now stored in the new variable 'county_count'.

# ### Explanation #9 
# Below I convert the above data into an actual data frame.

# In[49]:


# convert the series into a data frame
county_count = county_count.reset_index()
county_count


# #### Output #8
# The above series is now in the form of a data frame.

# ### Explanation #10
# Below, I am going to do a very simple plot of the data using the command.plot

# In[50]:


# plot the data frame
county_count.plot()


# #### Output #9
# The output of the .plot() operation is a line graph.

# ### Explanation #11
# Below, I will run a query on the data in order to practice filtering it.
#     

# In[56]:


# run .query to filter the data
calenviroscreen.query("ZIP == 90024'")


# #### Output #10
#  This should provide a filtered version of the data

# In[ ]:




