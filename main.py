# Importing the random library to generate random numbers
import random

# Importing resources to set rock, paper, scissors ASCII art from the resources file
import resources

# Print a welcome message and the rock, paper, scissors ASCII art
print("Welcome to the Rock, Paper, Scissors game.")
print("==============================================")
# Print rock, paper, and scissors in a single line separated by ' | '
print(resources.rock, resources.paper, resources.scissors, sep=' | ')
print("==============================================")

# Store the ASCII art in a list for easy access
info = [resources.rock, resources.paper, resources.scissors]

# Initialize variables to keep track of the user's and computer's wins
user_wins = 0
computer_wins = 0


# Function to display scores and ask the user if they want to continue playing
def remember():
    print("==============================================")
    game_continue = input("Do you want to see scores? Type 'Yes' or 'No': ").lower()
    print("==============================================")
    if game_continue == "yes":
        # Display the user's score
        user_score = "User Score"
        user_score_len = len(user_score) + 4
        print("+" + "-" * (user_score_len - 2) + "+")
        print("| " + user_score + " |" + ":", user_wins)
        print("+" + "-" * (user_score_len - 2) + "+")

        # Display the computer's score
        computer_score = "Computer Score"
        computer_score_len = len(computer_score) + 4
        print("+" + "-" * (computer_score_len - 2) + "+")
        print("| " + computer_score + " |" + ":", computer_wins)
        print("+" + "-" * (computer_score_len - 2) + "+")

        # Loop to ask the user if they want to continue playing
        while True:
            continue_the_game = input("Do you want to continue? Type 'Yes' or 'No': ").lower()
            if continue_the_game == "yes":
                print("Let's go :)")
                return main()  # Restart the game loop

            elif continue_the_game == "no":
                print("Thanks for playing. Bye :)")
                quit()  # Exit the game

            elif continue_the_game.isdigit():
                print('||| Please type Yes or No |||')
                continue  # Prompt again if the input is a number

    elif game_continue.isdigit():
        print("||| Please enter a string |||")
        return remember()  # Prompt again if the input is a number

    else:
        print("Okay. So keep playing...")
        return main()  # Continue the game if the user doesn't want to see scores


# Function to ask the user if they want to start playing
def before_start():
    playing = input("Do you want to play? Type 'Yes' or 'No': ").lower()
    if playing == "yes":
        print("Please wait....")
        print("Okay. So let's do this....")
        print('==========================')
    elif playing == "no":
        print("Thank You, Bye.")
        quit()  # Exit the game if the user doesn't want to play
    elif playing.isdigit():
        print("||| Please type Yes or No |||")
        return before_start()  # Prompt again if the input is a number

# Call the before_start function to start the game
before_start()


# Main function to handle the game logic
def main():
    global user_wins, computer_wins  # Use global variables to track wins
    should_continue = True

    while should_continue:
        try:
            # Get the user's choice and print the corresponding ASCII art
            user_choice = int(input("Please choose: 1.Rock 2.Paper 3.Scissors: "))
            user_choice_info = info[user_choice - 1]
            user_choice_txt = f"You chose: {user_choice_info}"
            length_user_choice_txt = len(user_choice_txt) + 4
            print("+" + "=" * (length_user_choice_txt - 2) + "+")
            print("| " + user_choice_txt + " |")
            print("+" + "=" * (length_user_choice_txt - 2) + "+")

        except ValueError:
            print("||| Please enter a number |||")
            continue  # Prompt again if the input is not a valid number

        # Generate a random choice for the computer and print the corresponding ASCII art
        computer_random_choice = random.randint(0, 2)
        computer_choice = info[computer_random_choice]
        computer_choice_txt = f"Computer chose: {computer_choice}"
        computer_choice_txt_length = len(computer_choice_txt) + 4
        print("+" + "-" * (computer_choice_txt_length - 2) + "+")
        print("| " + computer_choice_txt + " |")
        print("+" + "-" * (computer_choice_txt_length - 2) + "+")

        # Logic to determine the winner
        if user_choice - 1 == computer_random_choice:
            print("Draw")
        elif user_choice - 1 == 0 and computer_random_choice == 2:
            print("YOU WON!")
            user_wins += 1

        elif user_choice - 1 == 1 and computer_random_choice == 0:
            print("YOU WON!")
            user_wins += 1

        elif user_choice - 1 == 2 and computer_random_choice == 1:
            print("YOU WON!")
            user_wins += 1

        else:
            print("YOU LOSE!")
            computer_wins += 1
            return remember()  # Ask if the user wants to see scores and continue

    print("Good Bye.")

# Start the game if this script is run directly
if __name__ == '__main__':
    main()
