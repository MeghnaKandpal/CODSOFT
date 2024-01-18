import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def print_score(user_score, computer_score):
    print(f"Your Score: {user_score} | Computer Score: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        print("\nChoose: rock, paper, or scissors (or 'exit' to end)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            break

        if user_choice not in ('rock', 'paper', 'scissors'):
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print_score(user_score, computer_score)

    print("Thanks for playing!")

play_game()
