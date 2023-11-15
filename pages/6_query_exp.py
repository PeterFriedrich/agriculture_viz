# get query params from end of thing
# what the hell are query params

import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
    st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# why is this a thing?? # i guess it integrates with other stuff
# weird things like bookmarks

# 1. Instructions
st.header('1. Instruction')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL: `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`

Such that it becomes:
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`

For the offline app, it'll be something like this:
`http://localhost:8501/query_exp/?firstname=Jack&surname=Beanstalk`
''')

# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())

# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.experimental_get_query_params()["firstname"][0]
surname = st.experimental_get_query_params()["surname"][0]

st.write(f"Hello **{firstname} {surname}**, how are you?")