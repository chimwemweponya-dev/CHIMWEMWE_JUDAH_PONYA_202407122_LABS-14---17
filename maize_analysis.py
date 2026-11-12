#!/usr/bin/env python
# coding: utf-8

# # Maize Production Analysis
# ## Introduction
# This project analyses maize production
# using Python statistical computing tools.
# ## Objectives
# 1. Calculate average production.
# 2. Measure production variability.
# 3. Visualize maize production.
# 4. Interpret the results.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


np.random.seed(123)
production = np.random.normal(
    5, 1.2, 100
)
df = pd.DataFrame({ "Maize_Production": production
})
print(df.head())


# In[3]:


print(df.describe())


# In[4]:


plt.hist( df["Maize_Production"], bins=15, edgecolor="black"
)
plt.title("Maize Production Distribution")
plt.xlabel("Production (tonnes)")
plt.ylabel("Frequency")
plt.show()


# ## Interpretation
# The analysis provides information about
# average maize production and its variability.
# The histogram shows the distribution of
# the generated production observations.

# ## Conclusion
# Python statistical computing tools can
# be used to generate, analyse and visualize
# agricultural production data.

# In[ ]:




