import streamlit as st
from streamlit.components.v1 import html

# Streamlit UI setup
st.title("Binary Search Game in HTML/JavaScript")
st.write("In this game, I will guess the number you're thinking of using binary search.")

# Range input
min_range = st.number_input("Enter the minimum number:", min_value=1, value=1)
max_range = st.number_input("Enter the maximum number:", min_value=2, value=100)
max_attempts = st.number_input("Enter the maximum attempts:", step=1, value=5)

# Game state initialization
if 'attempts_used' not in st.session_state:
    st.session_state.attempts_used = 0
if 'game_initialized' not in st.session_state:
    st.session_state.game_initialized = False

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
        <p>Attempts used: <span id="attempt_used">0</span></p>
        <span id="result"></span>
    </div>
    
    <div id="buttons">
        <button class="button" onclick="tooLow()">Too Low</button>
        <button class="button" onclick="correctGuess()">Correct</button>
        <button class="button" onclick="tooHigh()">Too High</button>
    </div>

    <script>
        // Initialize variables
        let minRange = {min_range};
        let maxRange = {max_range};
        let attempts = 0;
        const maxAttempts = {max_attempts};
        let guess = Math.floor((minRange + maxRange) / 2);

        // Function to update display with the current guess and attempts used
        function updateDisplay() {{
            document.getElementById('guess').innerText = guess;
            document.getElementById('attempt_used').innerText = attempts;
        }}

        // Game logic for "Too Low"
        function tooLow() {{
            if (attempts >= maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
                return;
            }}
            minRange = guess + 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
            checkGameOver();
        }}

        // Game logic for "Too High"
        function tooHigh() {{
            if (attempts >= maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
                return;
            }}
            maxRange = guess - 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
            checkGameOver();
        }}

        // Game logic for "Correct Guess"
        function correctGuess() {{
            document.getElementById('result').innerText = 'I won! I guessed your number!';
        }}

        // Check if game is over
        function checkGameOver() {{
            if (attempts >= maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
            }}
        }}

        // Initialize the display with the first guess
        updateDisplay();
    </script>
</body>
</html>
"""

# Button to start the game
if st.button("Start Game"):
    st.session_state.game_initialized = True
    st.session_state.attempts_used = 0  # Reset attempts when the game starts
    html(binary_search_game_html, height=500)
