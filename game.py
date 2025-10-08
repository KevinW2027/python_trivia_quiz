import random
import sys 

anime_trivia = [
    {
        'question': 'In Attack on Titan, which main character has never obtained the power of Titans?',
        'answer': 'C',
        'options': ['A) Eren',
                    'B) Armin',
                    'C) Mikasa',
                    'D) Reiner']
    },
    {
        'question': "Which anime features the quote 'I am justice!'?",
        'answer': 'A',
        'options': ['A) Death Note', 'B) Code Geass', 'C) Psycho-Pass', 'D) Attack on Titan']
    },
    {
        'question': "In Naruto, what is the name of Naruto’s father?",
        'answer': 'B',
        'options': ['A) Sasuke Uchiha', 'B) Minato Namikaze', 'C) Jiraiya', 'D) Kakashi Hatake']
    },
    {
        'question': 'Which of the following is NOT one of the original Pokémon starter options in Pokémon Red and Blue?',
        'answer': 'C',
        'options': ['A) Charmander', 'B) Squirtle', 'C) Pikachu', 'D) Bulbasaur']
    },
    {
        'question': 'What does the organization “NERV” primarily fight against in Neon Genesis Evangelion?',
        'answer': 'A',
        'options': ['A) Angels', 'B) Demons', 'C) Titans', 'D) Shadows']
    }, 
    {
        'question': 'What is the main weapon used by Ichigo Kurosaki in Bleach?',
        'answer': 'A',
        'options': ['A) Katana', 'B) Zanpakutō', 'C) Kunai', 'D) Shuriken']
    },
    {
        'question': "In Spy x Family, what is Anya’s special ability?",
        'answer': 'D',
        'options': ['A) Super strength', 'B) Invisibility', 'C) Time travel', 'D) Telepathy']
    },  
    {
        'question': 'In Your Name (Kimi no Na wa), what unusual phenomenon connects the two main characters?',
        'answer': 'B',
        'options': ['A) Telepathy', 'B) Body swapping', 'C) Dream sharing', 'D) Parallel universes']
    },
    {
        'question': 'What’s the name of the pirate crew led by Monkey D. Luffy in One Piece?',
        'answer': 'B',
        'options': ['A) Red Hair Pirates', 'B) Straw Hat Pirates', 'C) Whitebeard Pirates', 'D) Blackbeard Pirates']
    },
    {
        'question': 'In Demon Slayer, what is Nezuko Kamado’s special ability?',
        'answer': 'B',
        'options': ['A) Controlling water', 'B) Blood Demon Art', 'C) Swordsmanship', 'D) Art of breathing']
    }
]

def ask_question(question, options, answer):
    print(question)
    for option in options:
        print(option)
    
    while True:
        choice = input("Enter your answer (A, B, C, or D): ")
        if choice.upper().strip() in ['A', 'B', 'C', 'D']:
            if choice == answer: 
                print('Correct!')
                return True
            else: 
                print('Incorrect! The correct answer was ' + answer + '.')
                return False 
        else:
            print('Invalid input!') 

def score_percent(total_questions, num_correct):
    return round((num_correct / total_questions) * 100, 2)

def main():
    print("Starting a new Anime Trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

    score = 0
    random.shuffle(anime_trivia)

    for que in anime_trivia: 
        if ask_question(que['question'], que['options'], que['answer']):
            score += 1

    total_q = len(anime_trivia)
    percent = score_percent(total_q, score)
    print(f'Quiz complete! You answered {score} out of {total_q} questions correctly.')
    print(f'Your final score is {percent}%')
    
    if percent == 100:
        print('Perfect! You aced the quiz!')
    elif percent >= 80:
        print('Great job! You have decent knowledge!') 
    elif percent >= 60:
        print('Not bad! Just Passed!')
    else:
        print('Ummmm... Maybe watch some more...')

if __name__ == "__main__":
    main()