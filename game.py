import random
'''
**2.** Which of the following is NOT one of the original Pokémon starter options in *Pokémon Red and Blue*?
A) Charmander
B) Squirtle
C) Pikachu
D) Bulbasaur

---

**3.** In *Naruto*, what is the name of Naruto’s father?
A) Sasuke Uchiha
B) Minato Namikaze
C) Jiraiya
D) Kakashi Hatake

---

**4.** What is the main weapon used by *Ichigo Kurosaki* in *Bleach*?
A) Zanpakutō
B) Kunai
C) Katana
D) Shuriken

---

**5.** In *My Hero Academia*, what is the name of Deku’s Quirk?
A) All for One
B) One for All
C) Super Strength
D) Ultra Smash

---

**6.** Which anime features the quote “I am justice!”?
A) *Death Note*
B) *Code Geass*
C) *Psycho-Pass*
D) *Attack on Titan*

---

**7.** What kind of creature is *Totoro* in *My Neighbor Totoro*?
A) Forest spirit
B) Cat demon
C) Tanuki
D) Mountain god

---
---

**9.** In *Demon Slayer*, what is Nezuko Kamado’s special ability?
A) Controlling water
B) Blood Demon Art
C) Swordsmanship
D) Fire breathing

---

**10.** What’s the name of the pirate crew led by Monkey D. Luffy in *One Piece*?
A) Red Hair Pirates
B) Straw Hat Pirates
C) Whitebeard Pirates
D) Blackbeard Pirates

---



'''
anime_trivia = [
    {
        'question':'In *Attack on Titan*, Which main character has never obtained the power of Titans?',
        'answer':'A',
        'options':['A) Eren',
                   'B) Armin',
                   'C) Mikasa',
                   'D) Arnie']

    },
    {
        'question':"Which anime features the quote'I am justice!'?",
        'answer':'A',
        'options': ['A) Death Note', 'B) Code Geass', 'C) Psycho-Pass', 'D) Attack on Titan']
    }
    {
        'question': "In *Naruto*, what is the name of Naruto’s father?",
        'answer':'B',
        'options': ['A) Sasuke Uchiha', 'B) Minato Namikaze', 'C) Jiraiya', 'D) Kakashi Hatake']

    }
    {
        'question': 'Which of the following is NOT one of the original Pokémon starter options in Pokémon Red and Blue?',
        'answer':'C',
        'options': ['A) Charmander', 'B) Squirtle', 'C) Pikachu', 'D) Bulbasaur']

    }
    {
        'question': 'What does the organization “NERV” primarily fight against in Neon Genesis Evangelion?',
        'answer':'A',
        'options': ['A) Angels', 'B) Demons', 'C) Titans', 'D) Shadows']

    }   
    {
        'question': 'What is the main weapon used by Ichigo Kurosaki in Bleach?',
        'answer':'A',
        'options': ['A) Katana', 'B) Zanpakutō', 'C) Kunai', 'D) Shuriken']

    }
    {
        'question': "In *Spy x Family*, what is Anya’s special ability?",
        'answer':'D',
        'options': ['A) Super strength', 'B) Invisibility', 'C) Time travel', 'D) Telepathy']

    }  
    {
        'question': 'In *Your Name (Kimi no Na wa)*, what unusual phenomenon connects the two main characters?',
        'answer':'B',
        'options': ['A) Telepathy', 'B) Body swapping', 'C) Dream sharing', 'D) Parallel universes']

    }
    {
        'question': 'In *Your Name (Kimi no Na wa)*, what unusual phenomenon connects the two main characters?',
        'answer':'B',
        'options': ['A) Telepathy', 'B) Body swapping', 'C) Dream sharing', 'D) Parallel universes']

    }
]


def main():
    print("Starting a new Trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

main()
