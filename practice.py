import random

options = ("rock", "paper", "scissors")

while True:
    player = input("Enter a choice (rock, paper, scissors): ")
    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    outcome = "It's a tie!" if player == computer else "You win! Congratulations!" if (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
    ) else "You lose!"

    print(outcome)

    if input("Play again? (y/n): ").lower() != "y":
        break

print("Thanks for playing.")
