# st.session state
"""
A session is defined as access to streamlit in a tab.
Each tab is a new session. Whole app reruns on interaction.
Each rerun is blank slate. Need session saving.
- session state lets you share variables between runs
- also can use callbacks, what ev they are.
"""
import streamlit as st

st.title("st.session_state")
st.write("""
        It appears that `st.session_state` lets you like,
         dot notation some objects it stores inside the module?.
         These just get shared between runs. 
         """)

def lbs_to_kg():
    # convert kg a val based on lbs
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    # convert lbs a val based on kg
    st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
# number input, into columns?
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms", key="kg", on_change = kg_to_lbs)



st.header("Output:")
st.write("Can just print out the st.session_state object:", st.session_state)
