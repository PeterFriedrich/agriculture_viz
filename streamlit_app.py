# streamlit app test

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# new button script, can you split
# up the streamlit script?
st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# import in other script here?
st.header('st.write')

# Example 1 emoji?
st.write('Hello, World*!* :sunglasses:')

#Example 2 just write an int
st.write(1234)

# Example 3: directly write dataframe
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 5: Apparently Altair is supported
# random dataframe
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

# altair char, circles? looks cool
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# you "write" the chart??
st.write(c)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)