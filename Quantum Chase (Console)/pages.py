import os
from user import User

user = User()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 

def page1_menu():
    print("Q U A N T U M   C H A S E\n")
    print("1. Login")
    print("2. Register")
    print("3. Exit\n")

    return int(input("Enter your choice: "))


def home_menu():
    clear()
    main_menu = ['Q U A N T U M   C H A S E\n', 'Play', 'Settings', 'Tutorial',
                 'Back\n']

    for i, menu in enumerate(main_menu):
        if i == 0:
            print(menu)
        else:
            print(f"{i}. {menu}")

    return int(input("Type your option: "))


def display_settings():
    clear()
    print("S E T T I N G S\n")
    print("1. Change username")
    print("2. Change password")
    print("3. Updates")
    print("4. Back")

    return int(input("\nEnter your choice: "))


def display_updates():
    clear()
    print("U P D A T E S\n")
    print("\033[4mComing Soon:\033[0m")
    print("\nAlmanac")
    print("\tthis is a feature that will serve as a handbook for our users along their journey in our program. \nIt will showcase the answered questions for review and other purposes.")
    print("\nPlaques")
    print("\tthis feature will be created in the future to award outstanding players in their accomplishments. \nThis features a printed plaque for collection purposes.")
    print("\nUser Interface and Design")
    print("\tA more profound and engaging interface design awaits.")

    back = input("\nPress B for Back: ")

    if back == "B":
        return "B"

def display_tutorial():
    clear()
    print("""\n\033[4mHow To Play Quantum Chase:\033[0m

    Welcome to Quantum Chase: Hunt For Victory In The Quantum Realm! This web-based quiz game is designed to test 
    your knowledge of the 17 Sustainable Development Goals and take you on a journey through the quantum realm. 

    Here\'s how to play: 
    
    1. Choose your Topic: The program will showcase all 17 SDGs as topics for the user to enjoy.
    
    2. Answer Questions: Once you have selected your chosen topic, you will be presented with the sets of questions 
    that you must answer. It is a multiple choice type of quiz where the users can choose the answer among the 
    options. After answering the first set of questions, the difficulty will increase. Once the hardest difficulty 
    has been successfully completed, the scores will be tallied.
    
    3. Collect Trophies: As you progress through the game, you can earn trophies by completing the quizzes and through 
    various tasks. The collected trophies will be presented in the trophy area for display.
    
    4. Explore The Quantum Realm: Quantum Chase: Hunt For Victory In The Quantum Realm takes you on a journey about 
    the past and possible future of our real world. Explore the quantum realm and learn about the events and 
    phenomena connected to the 17 Sustainable Development Goals that exist or have existed. 
    
    5. Challenge Yourself: The game is designed to be challenging and educational. Challenge yourself to learn more 
    about the Sustainable Development Goals and push yourself to the limits of your knowledge.
    
    6. Share with Friends: Invite your friends to play Quantum Chase: Hunt For Victory In The Quantum Realm and 
    compete against each other to see who can reach the highest level and earn the most rewards.
    
    
    Thank you for playing Quantum Chase: Hunt For Victory In The Quantum Realm. We hope you enjoy the game and learn 
    something new about the 17 Sustainable Development Goals.
    
    """)
    
    back = input("Press B for Back: ")

    if back == "B":
        return "B"
