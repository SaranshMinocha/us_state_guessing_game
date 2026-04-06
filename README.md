🗺️ U.S. States Guessing Game
A desktop quiz game built with Python and Turtle Graphics. Type in U.S. state names and watch them appear on the map — see how many you can get before you give up.

📸 Demo
Show Image

🚀 How It Works

A blank U.S. map loads on screen
A dialog box prompts you to guess a state name
Correct guesses are written directly onto the map at the state's coordinates
Type exit at any time to quit — a list of states you missed will print to the console
Game ends when all 50 states are guessed


🛠️ Tech Stack
ToolPurposePython 3Core languageTurtle GraphicsMap rendering & text placementPandasReading state coordinate data from CSV

📁 Project Structure
us_state_guessing_game/
├── main.py                  # Game logic
├── blank_states_img.gif     # U.S. map background image
├── 50_states.csv            # State names + x/y coordinates
└── README.md
50_states.csv format
state,x,y
Alabama,139,-77
Alaska,-204,-170
...

⚙️ Setup & Run
1. Clone the repo
bashgit clone https://github.com/SaranshMinocha/us_state_guessing_game.git
cd us_state_guessing_game
2. Install dependencies
bashpip install pandas

turtle is part of Python's standard library — no install needed.

3. Run the game
bashpython main.py

🎮 Controls
InputActionState nameGuess a state (case-insensitive)exitQuit and print missed states to console

📌 Known Limitations

Input is case-sensitive after .capitalize() — only works if you type the first letter lowercase or correctly capitalized (e.g. new york → New york fails, New York needed)
No duplicate guess detection — you can re-enter the same state and it won't tell you
Score counter doesn't increment for wrong guesses (intended behavior)


🧠 What I Learned

Using Turtle's textinput() for interactive dialogs
Navigating a pandas DataFrame by column value to fetch coordinates
Rendering text at precise x/y positions on a background image with Turtle


👤 Author
Saransh Minocha
GitHub
