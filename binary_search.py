import streamlit as st
import random
from streamlit.components.v1 import html

# Streamlit UI setup
st.title("Binary Search Game in HTML/JavaScript")
st.write("In this game, I will guess the number you're thinking of using binary search.")

# Range input
min_range = st.number_input("Enter the minimum number:", min_value=1, value=1)
max_range = st.number_input("Enter the maximum number:", min_value=2, value=100)

# Game state initialization
if 'game_initialized' not in st.session_state:
    st.session_state.game_initialized = False

if 'target' not in st.session_state:
    st.session_state.target = random.randint(min_range, max_range)

# HTML + JavaScript code for the binary search game
binary_search_game_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Search Game</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
        }}
        .button {{
            padding: 10px 20px;
            font-size: 16px;
            margin: 5px;
            cursor: pointer;
            border: none;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
        }}
        .button:hover {{
            background-color: #45a049;
        }}
    </style>
</head>
<body>
    <h2>Welcome to the Binary Search Game!</h2>
    <p>Think of a number between {min_range} and {max_range}.</p>
    <p>I'll guess it using binary search. You just need to tell me if my guess is "too low", "too high", or "correct".</p>

    <div id="guessing-area">
        <p>My guess is: <span id="guess">N/A</span></p>
        <p>Remaining range: <span id="range">N/A</span></p>
    </div>
    
    <div id="buttons">
        <button class="button" onclick="tooLow()">Too Low</button>
        <button class="button" onclick="correctGuess()">Correct</button>
        <button class="button" onclick="tooHigh()">Too High</button>
    </div>

    <script>
        let minRange = {min_range};
        let maxRange = {max_range};
        let target = {st.session_state.target};  // The target number
        let guess = Math.floor((minRange + maxRange) / 2);
        let attempts = 0;

        function updateDisplay() {{
            document.getElementById('guess').innerText = guess;
            document.getElementById('range').innerText = minRange + " to " + maxRange;
        }}

        function tooLow() {{
            minRange = guess + 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
        }}

        function tooHigh() {{
            maxRange = guess - 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
        }}

        function correctGuess() {{
            if (guess === target) {{
                alert("Yay! I guessed the number " + target + " in " + (attempts + 1) + " attempts.");
            }} else {{
                alert("Something went wrong. Please make sure the range is correct.");
            }}
        }}

        updateDisplay();
    </script>
</body>
</html>
"""

# Embed HTML and JavaScript inside Streamlit
if st.button("Start Game"):
    st.session_state.game_initialized = True
    html(binary_search_game_html, height=500)

