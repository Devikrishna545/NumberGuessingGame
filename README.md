# 🎮 Number Guessing Game

A simple and fun Python-based number guessing game that challenges players to find a secret number between 1 and 100 using helpful hints!

## 📝 Description

This is a beginner-friendly Python project designed to help understand basic programming concepts including:
- Random number generation
- User input handling
- Conditional logic
- Functions and modular code structure
- While loops

The game generates a random secret number and provides hints ("Hot" or "Cold") to help you guess the correct number.

## 🎯 How It Works

1. The program generates a random secret number between 1 and 100
2. You enter your guess
3. The game provides hints based on your guess:
   - **"Right"** - You guessed the secret number! 🎉
   - **"Hot"** - Your guess is within 10 numbers of the secret number 🔥
   - **"Cold"** - Your guess is more than 10 numbers away from the secret number ❄️
4. Keep guessing until you find the secret number!

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Devikrishna545/NumberGuessingGame.git
```

2. Navigate to the project directory:
```bash
cd NumberGuessingGame
```

### Running the Game

Simply run the Python file:
```bash
python "Number Guessing Game.py"
```

## 🎮 Game Example

```
Please enter your guessed number: 50
Cold
Please enter your guessed number: 75
Hot
Please enter your guessed number: 80
Hot
Please enter your guessed number: 78
Right
You guessed right!, the secret number is 78
```

## 🏗️ Code Structure

The project consists of three main functions:

- **`generateRandomNumber()`** - Generates a random number between 1 and 100
- **`giveHint(guess_number, secret_number)`** - Compares the guessed number with the secret number and returns appropriate hints
- **`getSecretNumber()`** - Main game loop that handles user input and game flow

## 🎓 Learning Outcomes

This project helps you understand:
- Working with Python's `random` module
- Function definitions and returns
- Conditional statements (if/elif/else)
- User input with `input()` function
- Type conversion with `int()`
- While loops for continuous execution
- String formatting with f-strings

## 🤝 Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add difficulty levels (easy, medium, hard)
- Track the number of attempts
- Implement a scoring system
- Add a replay option
- Set custom number ranges

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

**Devikrishna545**
- GitHub: [@Devikrishna545](https://github.com/Devikrishna545)

## ⭐ Show Your Support

If you found this project helpful, please give it a star! ⭐

---

Happy Gaming! 🎮
