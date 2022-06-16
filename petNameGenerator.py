from time import sleep
import random

names = ["Courtney", "Jack", "Sydney", "Bob",
         "Josh", "Maryanne", "Snoop", "Jennifer", "Akim", "Bella", "Luna", "Lucy", "Daizy", "Zoe", "Lily", "Lola", "Bailey", "Stella", "Molly", "Oliver", "Leo", "Milo", "Charlie", "Max", "Simba", "Jack", "Loki", "Ollie", "Jasper"]

# print(names)

random_name = random.choice(names)


def petNameGenerator():
    print("** Generating pet name **")
    sleep(1)

    print("*** Finishing pet name generation ***")
    sleep(1)
    print("                  ")
    print("---------------------------------------")
    print(f"Your generated pet name is {random_name}")
    print("---------------------------------------")
    print("                  ")


def goodbye():
    print("                  ")
    print("Goodbye!")
    print("---------------------------")
    print("                  ")
    print("Thanks for using Pet Name Generator by GOLDEN EKPENDU")
    print("                  ")
    print("--------------------------")


def anotherNameGenerator():
    another_name = input(
        "Would you like another name suggestion? Y/N: ").upper()
    print("********************")

    if another_name == "Y":
        petNameGenerator()


random_name = random.choice(names)


def petNameGame():
    while True:

        favouriteAnimals = input("What is your favourite animal? ")

        while favouriteAnimals == None:
            favouriteAnimals = input("What is your favourite animal? ")

        print(f"Your favourite animal is {favouriteAnimals}")

        pet_name = input("Would you like a pet name? Y/N: ").upper()
        print("---------------------")

        if pet_name == "Y":
            petNameGenerator()

        else:
            print("Sad to see you leave :( ")
            goodbye()
            break

        anotherNameGenerator()
        goodbye()
        break


petNameGame()
