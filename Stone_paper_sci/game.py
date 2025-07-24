import random

# A simple Stone, Paper, Scissors game.
# We'll use a standard mapping for clarity:
# Stone: 0
# Paper: 1
# Scissor: 2

def check(comp, user):
    """
    Checks the winner of a Stone, Paper, Scissors round.
    Returns:
         0 if it's a draw.
         1 if the user wins.
        -1 if the computer wins.
    """
    # Draw condition
    if comp == user:
        return 0

    # User winning conditions
    # User (Paper: 1) beats Comp (Stone: 0)
    # User (Scissor: 2) beats Comp (Paper: 1)
    # User (Stone: 0) beats Comp (Scissor: 2)
    if (user == 1 and comp == 0) or \
       (user == 2 and comp == 1) or \
       (user == 0 and comp == 2):
        return 1

    # If it's not a draw and the user didn't win, the computer must have won.
    return -1

# --- Main Game Logic ---

# A dictionary to map numbers to their names for easy printing
choice_names = {0: "Stone", 1: "Paper", 2: "Scissor"}

# Get computer's choice
# random.randint(0, 2) will pick 0, 1, or 2 randomly
comp_choice = random.randint(0, 2)

# Get user's input
try:
    user_choice = int(input("Enter your choice (0 for Stone, 1 for Paper, 2 for Scissor): "))

    # Validate user input
    if user_choice not in [0, 1, 2]:
        print("Invalid choice! Please enter 0, 1, or 2.")
    else:
        print("---")
        print(f"Your choice: {choice_names[user_choice]}")
        print(f"Computer's choice: {choice_names[comp_choice]}")
        print("---")

        # Determine the winner by calling the check function
        result = check(comp_choice, user_choice)

        if result == 0:
            print("It's a Draw! 🤝")
        elif result == 1:
            print("Congratulations! You Win! 🎉")
        else:
            print("Sorry, the Computer Wins. 💻")

except ValueError:
    print("Invalid input! You must enter a number.")