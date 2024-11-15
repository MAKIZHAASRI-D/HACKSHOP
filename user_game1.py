import streamlit as st
from streamlit_option_menu import option_menu
import random

def game():
    if st.button("Check"):
        st.session_state.attempted += 1
        if guessing_number ==  st.session_state.random_number:
            st.write(f"the number that should be guessed is { st.session_state.random_number}")
            st.success("You have won!")
        else:
            remaining_attempts = no_of_attempts - st.session_state.attempted
            if remaining_attempts > 0:
                if guessing_number>st.session_state.random_number:
                    st.warning(f"Wrong guess! You have {remaining_attempts} attempts left.")
                    st.write("your guess is too high!")
                if guessing_number<st.session_state.random_number:
                    st.warning(f"Wrong guess! You have {remaining_attempts} attempts left.")
                    st.write("your guess is too low!")
            else:
                st.error(f"You've used all your attempts! The correct number was {st.session_state.random_number}.")
                st.session_state.attempted = 0
                st.write("Game over! Please refresh to play again.")



st.title("INTUITION ZONE GAME" )
st.write("##")
st.header("THE ACTUAL GAME BEGINS HERE........")
with st.container():
        st.write("RANGE SETUP")
        st.write("##")
        min_range = st.number_input("Enter the minimum range:", key="min_range", step=1)
        max_range = st.number_input("Enter the maximum range:", key="max_range", step=1)
        if min_range >= max_range:
            st.error("Minimum range must be less than maximum range.")
        else:
            if 'random_number' not in st.session_state:
                st.session_state.random_number = random.randint(min_range, max_range)




        st.write("---")
        st.write("LIVES")
        st.write("##")
        no_of_attempts = st.number_input("Enter the number of attempts you want:", step=1,value=0)


        
        st.write("---")
        st.write("GUESS THE NUMBER")
        st.write("##")
        if 'attempted' not in st.session_state:
            st.session_state.attempted = 0
        if st.session_state.attempted < no_of_attempts:
            guessing_number = st.number_input(f"Enter your guess between {min_range} and {max_range}:", key="guess_input", value=0)
            if guessing_number<=max_range and guessing_number>=min_range:
                game()
            else:
                st.warning(f"enter the number which is within the range {min_range} and {max_range}")          