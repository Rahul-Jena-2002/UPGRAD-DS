import random

# Define the questions and answers
questions = {
    "The black box in a plane is orange.": "F",
    "Don't Be Cruel by Elvis Presley is 2 minutes 4 seconds long.": "F",
    "All polar bears are left-handed.": "T",
    "The Great Wall of China is visible from space.": "F",
    "The shortest war in history lasted only 38 minutes.": "T",
    "Pablo Picasso cut off his own ear.": "F",
    "The tallest mammal in the world is the elephant.": "F",
    "The currency of Japan is the yen.": "T",
    "The national animal of Scotland is the unicorn.": "T",
    "The first Apple computer was released in 1984.": "F"
}

# Define the additional features
difficulty = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

lives = 3

# Define a function to get a random question
def get_question():
    return random.choice(list(questions.keys()))

# Define a function to get the difficulty level of a question
def get_difficulty(question):
    if question in ["The black box in a plane is orange.", "The national animal of Scotland is the unicorn."]:
        return "easy"
    elif question in ["The tallest mammal in the world is the elephant.", "The first Apple computer was released in 1984."]:
        return "medium"
    else:
        return "hard"

# Define a function to check if a player's answer is correct
def is_correct(player_answer, correct_answer):
    return player_answer.lower() == correct_answer.lower()

# Define a function to get a player's answer
def get_answer(player):
    while True:
        answer = input(f"Player {player}, please enter your answer (T/F): ")
        if answer.lower() in ["t", "f"]:
            return answer.upper()
        else:
            print("Invalid answer. Please enter T or F.")

# Define a function to provide a swap option
def swap_question():
    global lives
    if lives > 0:
        print("You have used your swap option. Here is your new question:")
        lives -= 1
        return get_question()
    else:
        print("You do not have any more swaps left.")
        return None

# Define a function to calculate the score
def calculate_score(difficulty, is_correct):
    if is_correct:
        if difficulty == "easy":
            return 1
        elif difficulty == "medium":
            return 2
        else:
            return 3
    else:
        return 0

# Define the main function
def main():
    global lives
    
    print("Welcome to the True or False Game!\n")
    print("The rules of the game are as follows:")
    print("- You will be asked a series of true or false questions.")
    print("- If you get five correct answers in a row, you win the game.")
    print("- If you do not know the answer to a question, you can use a swap option.")
    print("- You have three lives. If you get a question wrong, you lose a life.")
    print("- The difficulty of the question determines the number of points you can earn.\n")
    
    # Initialize variables
    current_score = 0
    current_streak = 0
    current_question = get_question()
    
    # Loop until the game is over
    while True:
        print(f"Question: {questions[q_num]}")

        # Prompt player 1 for their answer
p1_ans = input("Player 1 - True or False (T/F): ").upper()
while p1_ans not in {"T", "F"}:
    p1_ans = input("Invalid input. Player 1 - True or False (T/F): ").upper()

# Prompt player 2 for their answer
p2_ans = input("Player 2 - True or False (T/F): ").upper()
while p2_ans not in {"T", "F"}:
    p2_ans = input("Invalid input. Player 2 - True or False (T/F): ").upper()

# Determine which player is correct, or if both are correct or incorrect
if p1_ans == answers[q_num] and p2_ans == answers[q_num]:
    print("You are both correct!")
    p1_score += 1
    p2_score += 1
    lives = 3
elif p1_ans == answers[q_num]:
    print("Player 1 is correct!")
    p1_score += 1
    lives = 3
elif p2_ans == answers[q_num]:
    print("Player 2 is correct!")
    p2_score += 1
    lives = 3
else:
    print("You are both wrong!")
    lives -= 1
    if lives == 0:
        print("Game over!")
        if p1_score > p2_score:
            print("Player 1 wins!")
        elif p2_score > p1_score:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        break

# Update and display scores
print(f"Player 1 score: {p1_score} | Player 2 score: {p2_score}")

# Check if a player has won
if p1_score == 5:
    print("Player 1 wins!")
    break
elif p2_score == 5:
    print("Player 2 wins!")
    break

# Prompt the user if they want to swap the question
if lives > 0:
    swap = input("Do you want to swap the question? (Y/N): ").upper()
    while swap not in {"Y", "N"}:
        swap = input("Invalid input. Do you want to swap the question? (Y/N): ").upper()
    if swap == "Y":
        q_num = (q_num + 1) % len(questions)
        print("Question swapped!")

