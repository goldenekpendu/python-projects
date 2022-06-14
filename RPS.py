import random

print("**** WELCOME TO MY SIMPLE RPS GAME! ****")
print("")

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors?: ")
        player = player.lower()

        if player == computer:
            print("Player: ", player)
            print("Computer: ", computer)
            print("It's a TIE!")

        elif player == "rock":
            if computer == "paper":
                print("Player: ", player)
                print("Computer: ", computer)
                print("Paper envelpes rock. You LOSE!")

            if computer == "scissors":
                print("Player: ", player)
                print("Computer: ", computer)
                print("Rock smashes scissors. You WIN!")

        elif player == "paper":
            if computer == "rock":
                print("Player: ", player)
                print("Computer: ", computer)
                print("Paper envelopes rock. You WIN!")

            if computer == "scissors":
                print("Player: ", player)
                print("Computer: ", computer)
                print("Scissors shreds paper. You LOSE!")

        elif player == "scissors":
            if computer == "rock":
                print("Player: ", player)
                print("Computer: ", computer)
                print("Rock smashes scissors. You LOSE!")

            if computer == "paper":
                print("Player: ", player)
                print("Computer: ", computer)
                print("Scissors shreds paper. You WIN!")

    play_again = input("Would you like to play again? YES/NO: ")
    play_again = play_again.upper()

    if play_again != "YES":
        break
print("----------------------")
print("Game over! Thanks for playing")
print("----------------------")

print("**** Simple RPS game by Golden Ekpendu ****")
