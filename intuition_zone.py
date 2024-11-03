import streamlit as st
from streamlit_option_menu import option_menu
import json
from  streamlit_lottie import st_lottie 
import random
from PIL import Image


user_game=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\user_game.py",title="start game")
pg=st.navigation(pages=[user_game])
#st.set_page_config(layout="wide")
st.title("INTUITION ZONE")
with st.container():
    selected=option_menu(
        menu_title=None,
        options=['instructions','user details','game'],
        icons=['code-slash','person','game'],
        orientation='horizontal',
    )
if selected=="instructions":
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header(""" INSTRUCTIONS""")
            st.write("##")
            st.subheader("""to be continued""")
        with col2:
            def lottie_loader(filepath):
                with open(filepath,'r',encoding="utf-8",errors="ignore") as f:
                    return json.load(f)
            lottie_instructions=lottie_loader("C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\Animation - 1730663135629.json")
            st_lottie(lottie_instructions)
    

if selected=="user details":
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header("USER DETAILS")
            name=st.text_input("YOUR NAME:",key="name")
            email=st.text_input("YOUR EMAIL:",key="email")  
            if 'login_password' not in st.session_state:
                st.session_state.login_password=random.randint(1,100)
            submit_button=st.button("submit")
            if submit_button:
                if not name and email:
                    st.error("INVALID NAME OR EMAIL")
                else:
                    st.success(f"YOUR LOGIN PASSWORD IS SUCCESSFULLY CREATED")
                    st.write(f"LOGIN PASSWORD IS {st.session_state.login_password}")
        with col2:
            def lottie_loader(filepath):
                with open(filepath,'r',encoding="utf-8",errors="ignore") as f:
                    return json.load(f)
            lottie_instructions=lottie_loader("C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\Animation - 1730662935306.json")
            st_lottie(lottie_instructions)
    

if selected=="game":
    with st.container():
        st.image("C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\Animation - 1730657782752.gif")
    with st.container():
        st.header("INTUITION ZONE GAME")
        login_password=st.number_input("LOGIN PASSWORD",key="password",step=1,value=0)
        submit_button=st.button("submit")
        if submit_button:
            if login_password==st.session_state.login_password:
                st.success("VALID PASSWORD")
                pg.run()
            
            else:
                st.error("INVALID PASSWORD")
    