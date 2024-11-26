#PANDAS LIBRARY

import pandas as pd
df=pd.read_csv("C:/Users/sumit/OneDrive/Documents/military.csv")
df

df.head()
df.tail()
df.shape
df.info
df.size
df.isna
df.describe
df.nunique

# NUMPY LIBRARY

import numpy as np
my_arr=np.array([11,22,55,44,66,99,54,23,14,25,77])
print(my_arr)

print(np.min(my_arr))
print(np.max(my_arr))
print(np.mean(my_arr))
print(np.std(my_arr))
print(np.median(my_arr))
print(np.percentile(my_arr,20))
print(np.stack(my_arr))
print(np.vstack(my_arr))
print(np.hstack(my_arr))


# MATPLOTLIB LIBRARY

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/sumit/OneDrive/Documents/military.csv")
df.plot()
#GRAPH


plt.show()
#NO RESULT


df.plot(kind='scatter', x='Active military', y='Total')
#GRAPH
