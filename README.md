# Terminal-Games 🎮

A fun collection of classic games playable in the terminal! Featuring interactive gameplay with multiple difficulty levels and AI opponents.

## Games Included

- **Snake** - Navigate your snake to eat food while avoiding walls and your own body
- **Tic Tac Toe** - Play against a friend or challenge the AI bot with Easy, Medium, or Impossible difficulty
- **Number Guessing** - Guess a random number between 1-100
- **Hangman** - Guess letters to uncover words before running out of attempts
- **Rock Paper Scissors** - Classic hand game against the computer

## Features

- 🤖 AI opponent with minimax algorithm for unbeatable Tic Tac Toe gameplay
- 🎯 Multiple difficulty levels (Easy, Medium, Impossible)
- 🎨 Interactive terminal UI with visual feedback
- ⚡ Real-time game updates and responsive controls
- 💾 Save and exit functionality

## Requirements

- Python 3.x

## Installation

```bash
git clone https://github.com/Python-Swift15/Terminal-Games.git
cd Terminal-Games
```

## Usage

```bash
python3 PY3terminalgames.py
```

Follow the on-screen menu to select a game and play!

## Game Controls

- **Snake**: Use `w/a/s/d` keys to move
- **Number Guess**: Enter numbers between 1-100
- **Hangman**: Guess one letter at a time
- **Rock Paper Scissors**: Type rock, paper, or scissors
- **Tic Tac Toe**: Enter position numbers 0-8

## Code Structure

- `loading_bar()` - Animated startup screen
- `tic_tac_toe()` - Main Tic Tac Toe game handler
- `snake()` - Real-time snake game
- `hangman()` - Word guessing game
- `number_guess()` - Number guessing game
- `rps()` - Rock Paper Scissors game
- `minimax()` - AI algorithm for optimal Tic Tac Toe moves

## Future Improvements

- Add score tracking and leaderboards
- Implement persistent save files
- Add more games (Minesweeper, 2048, etc.)
- Enhanced graphics with colored terminal output

## License

Open source - Feel free to take inspiration!
