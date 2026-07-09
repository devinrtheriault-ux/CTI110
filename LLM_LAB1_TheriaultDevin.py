# Devin Theriault
# 07/08/2026
# LLM_LAB1
# Using LLM


'''
This game uses LLM-Copilot to ask user to enter a difficulty rating.  Then it generates questions based on the difficulty rating the user chose.
The game then collects the users inputs(answers), then scores the quiz.  The game quiz then tells user their score and congradulates them.
The quiz game will also play a sound on completion, based on user's score at the end of the quiz.
'''

import sys
import time
import winsound

# ANSI color codes
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

# Quiz questions organized by difficulty
EASY_QUESTIONS = [
    {
        "question": "What is the name of the town where Stranger Things takes place?",
        "options": ["A) Hawkins", "B) Derry", "C) Castle Rock", "D) Wonderland"],
        "answer": "A"
    },
    {
        "question": "What is the name of the alternate dimension in Stranger Things?",
        "options": ["A) The Void", "B) The Upside Down", "C) The Dark World", "D) The Shadow Realm"],
        "answer": "B"
    },
    {
        "question": "What is Eleven's favorite food?",
        "options": ["A) Pizza", "B) Hamburgers", "C) Waffles", "D) Ice Cream"],
        "answer": "C"
    }
]

MEDIUM_QUESTIONS = [
    {
        "question": "What is the name of the lab where Eleven was held captive?",
        "options": ["A) Hawkins Laboratory", "B) Brenner Institute", "C) The Facility", "D) Project MKUltra"],
        "answer": "A"
    },
    {
        "question": "What year does Season 1 of Stranger Things take place?",
        "options": ["A) 1982", "B) 1983", "C) 1984", "D) 1985"],
        "answer": "B"
    },
    {
        "question": "What is the name of the creature that kills people in Season 1?",
        "options": ["A) The Demogorgon", "B) The Mind Flayer", "C) The Demodog", "D) Vecna"],
        "answer": "A"
    }
]

HARD_QUESTIONS = [
    {
        "question": "What is Dr. Martin Brenner's first name?",
        "options": ["A) Walter", "B) Henry", "C) Peter", "D) Martin"],
        "answer": "B"
    },
    {
        "question": "In Season 4, who is revealed to be the primary villain behind the Hawkins disasters?",
        "options": ["A) The Mind Flayer", "B) Vecna (Henry Creel)", "C) Billy Hargrove", "D) The Demogorgon"],
        "answer": "B"
    },
    {
        "question": "What is the name of the arcade where the kids frequently hang out?",
        "options": ["A) Starcourt Arcade", "B) The Game Den", "C) Scoops Arcade", "D) Starcourt Games"],
        "answer": "A"
    }
]

def play_perfect_sound():
    """Play a celebratory sound for perfect score."""
    try:
        # Ascending tones for perfect score
        winsound.Beep(523, 200)  # C note
        time.sleep(0.1)
        winsound.Beep(659, 200)  # E note
        time.sleep(0.1)
        winsound.Beep(784, 200)  # G note
        time.sleep(0.1)
        winsound.Beep(1047, 300)  # High C note
    except Exception as e:
        print(f"Could not play sound: {e}")

def play_great_sound():
    """Play a good sound for great score (66-99%)."""
    try:
        # Two ascending notes
        winsound.Beep(523, 250)  # C note
        time.sleep(0.1)
        winsound.Beep(784, 250)  # G note
    except Exception as e:
        print(f"Could not play sound: {e}")

def play_okay_sound():
    """Play a neutral sound for okay score (<66%)."""
    try:
        # Single note
        winsound.Beep(440, 300)  # A note
    except Exception as e:
        print(f"Could not play sound: {e}")

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write(CLEAR)
    sys.stdout.flush()

# Asks user to enter a difficulty level
def get_difficulty():
    """Ask user to select difficulty level."""
    clear_screen()
    print("=" * 60)
    print("WELCOME TO THE STRANGER THINGS QUIZ GAME!")
    print("=" * 60)
    print("\nSelect your difficulty level:\n")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard\n")
    
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_questions(difficulty):
    """Return the appropriate question set based on difficulty."""
    if difficulty == 1:
        return EASY_QUESTIONS
    elif difficulty == 2:
        return MEDIUM_QUESTIONS
    else:
        return HARD_QUESTIONS

def run_quiz(questions):
    """Run the quiz and collect answers."""
    clear_screen()
    print("=" * 60)
    print("STRANGER THINGS QUIZ - Let's Begin!")
    print("=" * 60 + "\n")
    
    answers = []
    
    for index, q in enumerate(questions, 1):
        print(f"\nQuestion {index} of {len(questions)}:")
        print(q["question"] + "\n")
        
        for option in q["options"]:
            print(option)
        
        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                answers.append({
                    "question": q["question"],
                    "user_answer": user_answer,
                    "correct_answer": q["answer"],
                    "is_correct": user_answer == q["answer"]
                })
                break
            print("Invalid choice. Please enter A, B, C, or D.")
        
        clear_screen()
    
    return answers

def display_results(answers):
    """Display the quiz results."""
    clear_screen()
    print("=" * 60)
    print("QUIZ RESULTS")
    print("=" * 60 + "\n")
    
    correct_count = 0
    
    for index, answer in enumerate(answers, 1):
        status = "✓ CORRECT" if answer["is_correct"] else "✗ INCORRECT"
        print(f"\nQuestion {index}: {answer['question']}")
        print(f"Your answer: {answer['user_answer']}")
        if not answer["is_correct"]:
            print(f"Correct answer: {answer['correct_answer']}")
        print(f"Status: {status}")
        print("-" * 60)
        
        if answer["is_correct"]:
            correct_count += 1
    
    score_percentage = (correct_count / len(answers)) * 100
    print("\n" + "=" * 60)
    print(f"FINAL SCORE: {correct_count}/{len(answers)} ({score_percentage:.1f}%)")
    print("=" * 60)
    
    # Play sound based on score performance
    if score_percentage == 100:
        play_perfect_sound()
        print("\n🎉 PERFECT SCORE! You're a Stranger Things expert! 🎉")
    elif score_percentage >= 66:
        play_great_sound()
        print("\n👍 Great job! You know your Stranger Things!")
    else:
        play_okay_sound()
        print("\n📺 Not bad! Time for a Stranger Things rewatch!")

def main():
    """Main function to run the quiz."""
    try:
        difficulty = get_difficulty()
        questions = get_questions(difficulty)
        answers = run_quiz(questions)
        display_results(answers)
        
        print("\nThanks for playing!")
    except KeyboardInterrupt:
        print("\n\nQuiz cancelled.")

if __name__ == "__main__":
    main()
