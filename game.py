import streamlit as st
import json
from streamlit_lottie import st_lottie
from PIL import Image
#st.set_page_config(page_title="GUESSING GAME",page_icon="wave",layout="centered")
intuition_game=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\intuition_zone.py",title="INTUITION ZONE GAME",default=True)
cybernetic_reign=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\cybernetic_reign.py",title="CYBERNETIC REIGN GAME")
user_game=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\user_game.py",title="user_game")
computer_reign=st.Page(page="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\computer_game.py",title="computer_reign")
pg=st.navigation(pages=[cybernetic_reign,intuition_game,user_game,computer_reign])
pg.run()
st.subheader("SELECT YOUR MODE.......")
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        with st.container():
            st.header("INTUITION ZONE")
        with st.container():
            def lottie_loader(filepath):
                with open(filepath,'r',encoding="utf-8",errors="ignore") as f:
                    return json.load(f)
            lottie_brain=lottie_loader("C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\Animation - 1730657782752.json")
            st_lottie(lottie_brain)
            #if st.button("USER GUESSING MODE",key="user_guess"):
             #   intuition_game.run()
    with right_column:
        with st.container():
            st.header("CYBERNETIC REIGN")
        with st.container():
            def lottie_loader(filepath):
                with open(filepath,'r',encoding="utf-8",errors="ignore") as f:
                    return json.load(f)
            lottie_computer=lottie_loader("C:\\Users\\L E N O V O\\Desktop\\HACKSHOP\\HACKSHOP\\Animation - 1730657624215.json")
            st_lottie(lottie_computer)
            #if st.button("COMPUTER GUESSING MODE"):
             #   cybernetic_reign.run()
                
        
            
