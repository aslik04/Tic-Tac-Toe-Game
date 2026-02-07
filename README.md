Tic-Tac-Toe-Game

A simple terminal-based Tic-Tac-Toe game in Python, built for practicing idiomatic Python and clean OOP design.

Features
	•	Human vs Human mode
	•	Human vs Bot mode
	•	3 bot difficulties:
	•	Easy: random moves
	•	Medium: win/block + center/corner preference
	•	Hard: Minimax (optimal play)

Why this project

This project is used to practice:
	•	idiomatic Python style
	•	clean class design and separation of concerns
	•	type hints and enums
	•	game loops, input validation, and state transitions
	•	basic AI decision logic (heuristics + minimax)

Requirements
	•	Python 3.10+ (for modern type hints)

Run

python3 game.py

How to Play
	•	Enter row and column numbers from 0 to 2
	•	Example move:
	•	Row: 1
	•	Col: 2
	•	Board symbols:
	•	X
	•	O
	•	. for empty

Project Structure
	•	Game: game loop, board state, win/draw logic
	•	Bot: difficulty-based move selection
	•	Minimax: hard-mode optimal strategy

Notes
	•	Invalid input is handled (non-integers / out-of-range / occupied cells)
	•	Supports replay and keeps score across rounds