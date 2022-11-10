import random

while True:
    user = input("Enter a choice (rock, paper, scissors): ")
    a = ["rock", "paper", "scissors"]
    c = random.choice(a)
    print(f"\nYou chose {user}, computer chose {c}.\n")
    if user == c:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if c == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if c == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if c == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

    