import streamlit as st
from streamlit.components.v1 import html


st.title("CYBERNETIC REIGN GAME" )
st.write("##")
st.header("THE ACTUAL GAME BEGINS HERE........")
st.write("#")
with st.container():
    min_range = st.number_input("Enter the minimum number:",step=1, value=1)
    max_range = st.number_input("Enter the maximum number:",step=1, value=100)
    max_attempts = st.number_input("Enter the maximum attempts:", step=1, value=5)
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
        .button{{
            padding: 10px 20px;
            font-size: 16px;
            margin: 5px;
            cursor: pointer;
            border: none;
            background-color:blue;
            color: white;
            border-radius: 5px;
        }}
        
        .button:hover {{
            background-color:red;}}
        .disabled {{
            background-color:black;
            cursor: not-allowed;
        }}
    </style>
</head>
<body>

    <div id="guessing-area">
        <p>My guess is: <span id="guess">N/A</span></p>
        <p>Attempts used: <span id="attempt_used">0</span></p>
        <span id="result"></span>
    </div>

      
    <div id="buttons">
        <button id="button1" class="button" onclick="tooLow()" >Too Low</button>
        <button id="button2" class="button" onclick="correctGuess()">Correct</button>
        <button id="button3" class="button" onclick="tooHigh()">Too High</button>
    </div>
    <script>
       let minRange = {min_range};
        let maxRange = {max_range};
        let attempts = 1;
        const maxAttempts = {max_attempts};
        let guess = Math.floor((minRange + maxRange) / 2);

        function updateDisplay() {{
            document.getElementById('guess').innerText = guess;
            document.getElementById('attempt_used').innerText = attempts;
        }}

        function disableButtons() {{
            document.getElementById('button1').disabled = true;
            document.getElementById('button2').disabled = true;
            document.getElementById('button3').disabled = true;
            document.getElementById('button1').classList.add("disabled");
            document.getElementById('button2').classList.add("disabled");
            document.getElementById('button3').classList.add("disabled");
        }}

        function tooLow() {{
            if (attempts >= maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
                disableButton();
                return;
            }}
            minRange = guess + 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
            checkGameOver();
        }}

        function tooHigh() {{
            if (attempts >=maxAttempts) {{
                document.getElementById('result').innerText = "Game Over! You've used all your attempts.";
                disableButtons();
                return;
            }}
            maxRange = guess - 1;
            guess = Math.floor((minRange + maxRange) / 2);
            attempts++;
            updateDisplay();
            checkGameOver();
        }}

         function correctGuess() {{
            document.getElementById('result').innerText = 'I won! I guessed your number!';
            disableButtons();
           }}

           updateDisplay();
        
    </script>
</body></html>"""

if st.button("Start Game"):
     html(binary_search_game_html, height=600)