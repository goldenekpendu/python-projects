def quizTips():
    print(""" Welcome to Wordle
    This is a game where you guess a 5 lettered word
    Some icons will be used to let you know your progress

    ❌✔➕🏁

    ❌ - you've got a character wrong
    ✔ - you've got a character correct
    ➕ - you're almost there
    🏁 - you've successfully completed the guess
    """)


quizTips()


def beginQuiz():
    number_of_guesses = 5
    hidden_word = "happy"

    while number_of_guesses > 0:

        message = str(input("Guess a 5 letter word:"))

        if (message == hidden_word):
            print("YOU WIN! 🕺🕺")
            break
        else:
            number_of_guesses = number_of_guesses - 1
            print(f"** you have {number_of_guesses} attempt(s) ,, ** \n")

            for character, word in zip(hidden_word, number_of_guesses):
                if character in hidden_word and character in hidden_word:
                    print(word + " ✔ ")

                elif word in word:
                    print(word + " ➕ ")

                else:
                    print(word + " ❌ ")


beginQuiz()
