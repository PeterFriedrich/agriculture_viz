import time
import streamlit as st

st.set_page_config(page_title="Progress", page_icon="📈")

# st.progress bar/??
# this seems to block all other stuff till it's done
st.title('st.progress')
with st.expander('About this app'):
    st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)
    #st.write(percent_complete) how to have it replace?
st.balloons()