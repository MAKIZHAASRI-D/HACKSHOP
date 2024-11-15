import streamlit as st

# User inputs
max_num = st.number_input("Enter the maximum range: ")  # Ensure max_num is non-negative
min_num = st.number_input("Enter the minimum range: ")  # Ensure min_num is non-negative
max_attempts = st.number_input("Enter the maximum attempts: ", min_value=1)  # Ensure max_attempts is positive

# Initialize session_state variables if they are not already set
if "machine_game" not in st.session_state:
    st.session_state.machine_game=True
    st.session_state.max_num = max_num
    st.session_state.min_num = min_num
    st.session_state.max_attempts = max_attempts
    st.session_state.no_of_attempts = 0  

# Handling invalid input: min_num should be less than or equal to max_num
    if st.session_state.min_num > st.session_state.max_num:
        st.error("The minimum number cannot be greater than the maximum number. Please adjust the values.")
    else:
    # Display max_attempts when input is valid
        st.write(f"Maximum attempts: {st.session_state.max_attempts}")

# Placeholder text for understanding the flow
    st.write("hello")
