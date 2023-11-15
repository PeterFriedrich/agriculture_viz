# streamlit app test

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

from datetime import time, datetime

# streamlit layout
st.set_page_config(
    layout="wide",
    page_title="Hello",
    page_icon="👋",
) # hard to see it off
st.title("How to layout your Streamlit app")
st.write("# Welcome to Streamlit!")
st.sidebar.success("Select a demo above.")
st.markdown("""
    Streamlit is cool.
     checkout [streamlit.io](https://streamlit.io)
    - 
""")

# everying inside expander goes in the feature.
with st.expander("About this app"):
    st.write("This app shows the various ways on how you can layout your Streamlit app.")
    # cool, can do the html image thing
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# sidebar features. Text input, selectbox etc.
st.sidebar.header("Input")
user_name = st.sidebar.text_input("What is your name?")
user_emoji = st.sidebar.selectbox("Choose an emoji", ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# shows outputs of sidebar inputs
st.header("Output")
col1, col2, col3 = st.columns(3)

# the columns means all 3 outputs are side by side
with col1:
    if user_name != "":
        st.write(f"👋 Hello {user_name}!")
    else:
        st.write("👈 Please enter your **name**!")
with col2:
    if user_emoji != "":
        st.write(f"{user_emoji} is your favorite **emoji**!")
    else:
        st.write("👈 Please choose an **emoji**!")
with col3:
    if user_food !="":
        st.write(f" **{user_food}** is your favorite **food**!")
    else:
        st.write("👈 Please choose your favorite **food**!")


# finally, file uploader. Default 200 mb limit.
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')

# secrets are weird. Maybe have to reboot the app each time?
# streamlit secrets, st.secrets
# store api keys, database passwords, etc.
st.title('st.secrets')
st.write("The secret phrase is:", st.secrets['message'])

# streamlit themes??
st.title('Customizing the theme of streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFF"
        font="monospace"
        """)

# fancy sidebar slider
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write("Selected number from slider widget is:", number)

# streamlit latex
st.header('st.latex')

st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{r^k{n}}{1-r}\right)
         ''')

#import ydata_profiling
#from streamlit_pandas_profiling import st_profile_report

# Streamlit Components
st.header('`streamlit_pandas_profiling`')

#df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
#pr = df.profile_report()
#st_profile_report(pr)

# st.checkbox app. Puts up checkboxes
st.header('st.checkbox')
st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more :icecream")

if coffee:
    st.write("Okay, here's some coffee :coffee")

if cola:
    st.write("Here you go :pop")

# st.multiselect widget select?
st.header('st.multiselect')

# weird multibox select widget
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)

# selectbox app flow. User selects colr, app prints color
st.header('st.selectbox')

# click box? dropdown? dropdown
option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green'))

st.write('Your Favorite color is', option)

# altair line chart
st.header('Line Chart')

# demo data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# slider demo, headers and subheaders.
st.header('st.slider')

# example 1d
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# example 2, range slider just add more
st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# example 3, sometimes putting value is easier
st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# example 4
st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

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