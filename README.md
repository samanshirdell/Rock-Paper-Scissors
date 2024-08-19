# Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors** game! This is a simple command-line implementation of the classic hand game, where you can play against the computer.

![Rock Paper Scissors](https://github.com/user-attachments/assets/bd2c5afd-ee09-4347-b5b5-f353c9a5ab15)

## Features

- Play the classic game against a computer opponent.
- The game displays rock, paper, and scissors using ASCII art.
- Keeps track of both user and computer scores.
- Option to view scores and continue playing after each round.
- Input validation to ensure valid choices are made.

## Getting Started

### Prerequisites

- Python 3.12

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/samanshirdell/Rock-Paper-Scissors.git

2. cd `Rock-Paper-Scissors`

### Running the Game

To start the game, simply run the following command:
```bash
python main.py
```

## How to Play

1. **Start the Game**: When you run the program, you'll be welcomed to the game.
2. **Choose to Play**: You’ll be prompted to type `Yes` if you want to play or `No` to exit the game.
3. **Select Your Move**: Choose your move by entering the corresponding number:
   - `1` for Rock
   - `2` for Paper
   - `3` for Scissors
4. **See the Result**: The computer will randomly choose its move, and the result of the round will be displayed, showing whether you won, lost, or if it was a draw.
5. **Continue or Exit**: After each round, you can choose to continue playing or exit the game.

## Example Gameplay

Here’s an example of how the game might look when you play it:

```plaintext
Welcome to the Rock, Paper, Scissors game.
==============================================
Rock | Paper | Scissors
==============================================
Do you want to play? Type 'Yes' or 'No': Yes
Please choose: 1.Rock 2.Paper 3.Scissors: 1
+==================+
| You chose: Rock  |
+==================+
+-------------------+
| Computer chose: Scissors |
+-------------------+
YOU WON!
```
### Project Structure

`main.py`: The main script that runs the game.
`resources.py`: Contains ASCII art for rock, paper, and scissors.

### Contributing

Contributions are welcome! If you'd like to improve this game or fix any issues, please feel free to fork the repository and submit a pull request.





