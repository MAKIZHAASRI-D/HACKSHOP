import streamlit as st
from streamlit_option_menu import option_menu
import random

st.title("CYBERNETIC REIGN GAME" )
st.write("##")
st.header("THE ACTUAL GAME BEGINS HERE........")
st.write("#")
with st.container():
        st.write("RANGE SETUP")
        st.write("##")
        user_input=st.number_input("enter the target number:",step=1,value=0,key="user_input")
        min_range=st.number_input("enter the minimum value:",step=1)
        max_range=st.number_input("enter the maximum value:",step=1)
        if min_range >= max_range:
            st.error("Minimum range must be less than maximum range.")
        else:
            if 'guess' not in st.session_state:
                st.session_state.guess = random.randint(min_range, max_range)
            st.write(f"my guess is { st.session_state.guess}")
        submit_button=st.button("reveal answer")
        if submit_button:
            if user_input==st.session_state.guess:
                st.write("i have won")
            else:
                st.write(f"the correct answer is {user_input}")
                st.write("you won")
                
    
        

