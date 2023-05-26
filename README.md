# Blackjack Terminal Game

This is a command-line implementation of the classic casino game Blackjack built for MacOS. It allows you to play Blackjack against the dealer using text-based input and output.

## Prerequisites

To run this game, you need to have Python 3 installed on your system.

## Getting Started

1. Clone the repository or download the code files to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the game:

```
python3 blackjack.py
```

4. Follow the on-screen instructions to play the game.

## Gameplay

The game follows the standard rules of Blackjack. You will be dealt two cards, and the dealer will also receive two cards, with one card facing down. The goal is to get a hand value as close to 21 as possible without exceeding it. Face cards are worth 10 points, and Aces can be worth 1 or 11 points.

You will be prompted to choose whether to "Hit" (draw another card) or "Stay" (end your turn) during your turn. The dealer will then reveal their hidden card and draw additional cards until their hand value is at least 17. The winner is determined by comparing the hand values.

The game supports features such as tracking your wallet balance, placing bets, and handling special cases like Blackjack and busts.

## Customization

You can customize certain aspects of the game by modifying the `Rules` class. The current customization options include:

- Minimum bet amount
- Starting amount in the player's wallet
- Payout ratio for getting Blackjack at the beginning of the round

Feel free to adjust these values to suit your preferences.

## License

This project is licensed under the BSD License. You can find the license details in the [LICENSE](LICENSE) file.

## Acknowledgments

- The game code was developed by Avery Seabolt.
- This project is inspired by the classic casino game Blackjack.

Feel free to modify and enhance the code as you see fit. Enjoy playing Blackjack in the terminal!