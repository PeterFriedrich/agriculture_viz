# st.cache is for optimization

# apparently this helps with loading data from the web,
# manipulating large datasets, or performing expensive 
# computations

# when you mark a function with the decorator it 
# make st check some stuff
# 1. The input params you called the func with
# 2. the value of any external variable used in func
# 3. The body of the func, 
# 4. The body of any function used inside the cached function

# if this is the first time it saw these, it runs the func
# but will also store results in a local cache.
# if the stuff is identical next time, can just check 
# the cache. It hashes all components.
# in memory, key-value store.
import streamlit as st
import numpy as np
import pandas as pd
from time import time

# st.cache is deprecated. Please use one of 
# Streamlit's new caching commands, st.cache_data or 
# st.cache_resource.

# caching example
st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

# put cache decorator
@st.cache_data()
def load_data_a():
    # makes a data frame, with random numbers
    df = pd.DataFrame(
        np.random.rand(2_000_000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_a())
#st.write(load_data_a())
#st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# not using cache
b0 = time()
st.subheader("Note using st.cache")

# no cache
def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2_000_000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
#st.write(load_data_b())
#st.write(load_data_b())
b1 = time()
st.info(b1-b0)

# the difference is when you re-run the app.
# the top time should lower, while the bottom 
# will stay similar