import time
import random


def print_pause(message, t):
    print(message)
    time.sleep(t)


def valid_input(prompt, option1, option2):
    response = input(prompt).lower()
    if option1 in response:
        return response
    elif option2 in response:
        return response
    else:
        print_pause("Sorry, I don't understand.", 2)


def intro():
    print_pause("You find yourself in the middle of Serengeti "
                "National Park in the middle of the night", 2)
    print_pause("In front of you are two passage ways", 2)
    print_pause("Enter 1 to head towards the nearest Maasai Village", 2)
    print_pause("Enter 2 to search for the camping site", 2)


def national_park():
    response = valid_input("Please enter 1 or 2: \n", "1", "2")
    if "1" in response:
        print_pause("You manage to find some Maasai folks in the village,"
                    " who are willing to help you get back to"
                    " the camping site", 2)
        print_pause("They ask you to spend the night at the village"
                    " and promise to guide you back in the morning", 2)
        print_pause("Enter 1 to spend the night in the village", 2)
        print_pause("Enter 2 to go back and search for the camping site", 2)
        response = input("Please enter 1 or 2: \n")
        if "1" in response:
            print_pause("You decide to spend the night at the village", 2)
            print_pause("The next morning a kind Maasai gentleman"
                        " guides you back to the camping site", 2)
            print_pause("Congratulations! You have reunited with your"
                        " friends at the camping site", 2)
            print_pause("You won the game!", 2)
            play_again()

        elif "2" in response:
            enemy_list = ["You get attacked by a pride of Lions!",
                          "You get attacked by a crash of Black Rhinos!"]
            print_pause("You head back to the forest", 2)
            print_pause(random.choice(enemy_list), 2)
            print_pause("You lost! :( ", 2)
            play_again()
        else:
            print_pause("Please try again! ", 2)
    elif "2" in response:
        enemy_list = ["You get attacked by a pride of Lions!",
                      "You get attacked by a crash of Black Rhinos!"]
        print_pause("You head towards the dense forest to look for"
                    " your friends at the camping site", 2)
        print_pause(random.choice(enemy_list), 2)
        print_pause("You lost! :(", 2)
        play_again()

    else:
        print_pause("Please try again!", 2)


def play_again():
    response = valid_input('Would you like to play again?(Y/N)\n',
                           "y", "n").lower()
    if "n" in response:
        print_pause("Thank you for playing! Goodbye!", 2)
    elif "y" in response:
        play_game()


def play_game():
    intro()
    national_park()
    play_again()


play_game()
