import time
from tqdm import tqdm

from pages import *
from quiz_generator import QuizGenerator
from user import User
from level_page import show_level, show_difficulty
from loadout import Loadout
 
user = User()

#sdg6 to sdg9 are not included due to not being able to locate the files

def load():
    total_chunks = 1024 // 64

    progress_bar = tqdm(total=total_chunks, unit='chunk', ncols=80)

    for _ in range(total_chunks):
        time.sleep(0.1)
        progress_bar.update(1)

    progress_bar.close()
    clear()

def page1_instances():
    clear()
    user_choice = page1_menu()
    clear()

    load()

    if user_choice == 1:
        user.login()
        home_instances()
    elif user_choice == 2:
        user.register()
        home_instances()
    else:
        exit()


def home_instances():
    while True:
        home_choice = home_menu()

        if home_choice == 1:
            quiz()
        elif home_choice == 2:
            settings_instances(display_settings())
        elif home_choice == 3:
            back = display_tutorial()
            if back == 'B':
                home_instances()
        elif home_choice == 4:
            page1_instances()
        


def loadout_instances():
    loadouts = Loadout()
    passive, skills= loadouts.start_loadout_selection()

    if passive == "1":
        passive = "Vitality Cascade"
    elif passive == "2":
        passive = "Aegis Flux"
    elif passive == "3": 
        passive = "Time Warp"
    elif passive == "4": 
        passive = "Unleashed Arsenal"
    elif passive == "5":
        passive = "Risky Refinement"


    return passive, skills


def settings_instances(choice):
    if choice == 1:
        user.change_username()
        user.login()
        home_instances()
    elif choice == 2:
        user.change_pass()
        user.login()
        home_instances()
    elif choice == 3:
        display_updates()
    elif choice == 4:
        home_instances()
    else:
        settings_instances(choice)



def quiz():
    sdg, description = show_level()
    difficulty = show_difficulty()
    passive, skills = loadout_instances()
    quiz_generator = QuizGenerator(f"quiz_data/sdg_{sdg}.json", f"{difficulty}")
    quiz_generator.analyze_passive(passive)
    quiz_generator.analyze_skills(skills)

    clear()
    quiz_generator.start_quiz()
    back = quiz_generator.end_page()
    if back == "B":
        home_instances()

    
page1_instances()