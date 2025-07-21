import time

# --- Data Structure Improvement ---
# It's better to group related data together. Instead of multiple separate lists,
# we use a single list of dictionaries. Each dictionary holds all the information

quiz_data = [
    {
        "question": "Current Railway Minister of India is",
        "options": ['Mamta Banarjee', 'Ram Vilash', 'Ashwini Vaishnaw', 'Piyush Goyal'],
        "answer": 'Ashwini Vaishnaw'
    },
    {
        "question": "Which god is also known as ‘Gauri Nandan’?",
        "options": ['Agni', 'Indra', 'Hanuman', 'Ganesha'],
        "answer": 'Ganesha'
    },
    {
        "question": "What does not grow on a tree according to a popular Hindi saying?",
        "options": ['Money', 'Flowers', 'Leaves', 'Fruits'],
        "answer": 'Money'
    },
    {
        "question": "Which city is known as the Pink City of India?",
        "options": ['Banglore', 'Maysore', 'Jaipur', 'Kochi'],
        "answer": 'Jaipur'
    },
    {
        "question": "Who wrote India's National Anthem?",
        "options": ['Rabindranath Tagore', 'Lal Bahadur Shastri', 'Chetan Bhagat', 'RK Narayan'],
        "answer": 'Rabindranath Tagore'
    },
    {
        "question": "How many major religions are there in India?",
        "options": [6, 7, 8, 9],
        "answer": 6  # The original answer was '6', which is ambiguous. Storing as an int is better.
    },
    {
        "question": "When is the National Hindi Diwas celebrated?",
        "options": ['13 September', '14 September', '14 July', '15 August'],
        "answer": '14 September'
    },
    {
        "question": "How many states are there in India?",
        "options": [28, 29, 31, 32],
        "answer": 28 # Storing numbers as int is better for comparison.
    },
    {
        "question": "Where is India Gate located?",
        "options": ['Agra', 'Punjab', 'Mumbai', 'New Delhi'],
        "answer": 'New Delhi'
    },
    {
        "question": "Who wrote Vande Mataram?",
        "options": ['Sarat Chandra Chattopadhyay', 'Rabindranath Tagore', 'Bankim Chandra Chatterjee', 'Ishwar Chandra Vidyasagar'],
        "answer": 'Bankim Chandra Chatterjee'
    }
]

# Prize money for each correct answer level.
rewards = [0, 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

def play_game():
    """
    Main function to run the quiz game.
    """
    money_won = 0
    print("--- Welcome to the Quiz Game! ---")
    print("Answer correctly to win prize money. The game ends on the first wrong answer.\n")
    time.sleep(2)

    # Use enumerate to get both the index (question_level) and the question data.
    for question_level, data in enumerate(quiz_data):
        current_prize = rewards[question_level + 1]
        print("------------------------------------------------------------------")
        print(f"Question {question_level + 1} for Rs. {current_prize}")
        print("------------------------------------------------------------------")
        print(f"Q: {data['question']}\n")

        # Print options clearly with numbers.
        for i, option in enumerate(data['options']):
            print(f"  {i + 1}. {option}")

        # --- Improved Input Handling ---
        user_input = input("\nEnter your answer (number or text): ").strip()
        
        # --- Simplified Answer Checking ---
        is_correct = False
        correct_answer_str = str(data['answer'])

        # Check if user entered the option number
        if user_input.isdigit():
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(data['options']):
                # Compare the chosen option with the correct answer
                if str(data['options'][choice_index]) == correct_answer_str:
                    is_correct = True
        
        # If not a valid number, check if they typed the answer text (case-insensitive)
        if not is_correct and user_input.lower() == correct_answer_str.lower():
            is_correct = True
            
        # --- Clearer Feedback and Game Flow ---
        if is_correct:
            money_won = current_prize
            print(f"\nCorrect Answer! You have won Rs. {money_won}\n")
            time.sleep(1)
        else:
            print(f"\nSorry, that's the wrong answer. The correct answer was: {data['answer']}")
            break # End the game on a wrong answer

    print("\n--- Game Over ---")
    if money_won > 0:
        print(f"Congratulations! You are taking home Rs. {money_won} !!!")
    else:
        print("Sorry, you didn't win any money. Better luck next time!")


# Start the game
play_game()