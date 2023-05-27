import json
from random import sample, shuffle, choice
from user import User

from pages import * 
 

class QuizGenerator:
    def __init__(self, sdg_path, difficulty):
        self.sdg_path = sdg_path
        self.difficulty = difficulty
        self.items = 15
        self.quiz = []
        self.hearts = 3
        self.points = 0
        self.status = ""
        self.usage_skill1 = self.usage_skill2 = self.usage_skill3 = 1
        self.skill1_show = self.skill2_show = self.skill3_show = ""
        self.vitality_counter = 0
        self.vitality_checker = False
        self.arsenal_checker = False
        self.aegis_checker = False
        self.refinement_checker = False
        self.resilient_checker = False
        self.passive = ""
        self.q_num = 1
        self.get_username = User()

    def get_questions(self):
        with open(self.sdg_path, 'r') as f:
            questions = json.load(f)

        filtered_questions = [q for q in questions if q['difficulty'] == self.difficulty]
        self.quiz = sample(filtered_questions, k=self.items)
    
    def analyze_passive(self, passive):
        self.passive = passive

        if passive == "Vitality Cascade":
            self.vitality_checker = True

        elif passive == "Aegis Flux":
            self.aegis_checker = choice([True, False, False])

        elif passive == "Unleashed Arsenal":
            self.arsenal_checker = True

        elif passive == "Risky Refinement":
            self.refinement_checker = True
            self.status = "Risky Refinement: More points and damage being received!"

    def analyze_skills(self, skills):
        skill_map = {
            "A": "Healstream Surge",
            "B": "Quantum Leap",
            "C": "Intuition Insight",
            "D": "Resilient Echo",
            "E": "Skill Resurgence"
        }

        self.skill1_show = skill_map[skills[0]]
        self.skill2_show = skill_map[skills[1]]

        if self.arsenal_checker:
            self.skill3_show = skill_map[skills[2]]


    def start_quiz(self):
        self.get_questions()

        for item in self.quiz:
            clear()
            if self.hearts < 0:
                self.hearts = 0
            elif self.hearts == 0:
                break

            question = f"{item['question']}\n"
            answer = item["answer"]

            choices = item["choices"].copy()
            shuffle(choices)
            choices_dict = {}
            letters = ["A", "B", "C", "D"]

            for i, choice in enumerate(choices):
                letter = letters[i]
                choices_dict[letter] = choice
                
            self.update_quiz(question, answer, choices_dict)

        if self.q_num == self.items + 1 and self.hearts > 0:
            with open(f"user_data/{self.get_username.get_username()}.json", "w") as f:
                data = json.load(f)

            if "almanac" in data:
                data["almanac"].extend(self.quiz)
            else:
                data["almanac"] = self.quiz

            with open(f"user_data/{self.get_username.get_username()}.json", 'w') as f:
                json.dump(data, f)
    

    def update_quiz(self, question, answer, choices_dict):
        clear()
        print(f"Hearts: {self.hearts}")
        print(f"Points: {self.points}")
        print(f"Status: {self.status}\n")

        print(f"\nPress 1 to use {self.skill1_show}. Usage: {self.usage_skill1}")
        print(f"Press 2 to use {self.skill2_show}. Usage: {self.usage_skill2}")
        print(f"Press 3 to use {self.skill3_show}. Usage: {self.usage_skill3}") if self.arsenal_checker else None

        print(f"\n\nQuestion {self.q_num}/{self.items}")
        print(f"{question}")
        self.q_num += 1

        for key, value in choices_dict.items():
            print(f"{key}. {value}\n")

        user_ans = input("\nYour answer: ").upper()
        self.check_answer(user_ans, question, answer, choices_dict)

    
    def check_answer(self, user_ans, question, answer, choices_dict):
        input_mapping = {
                "1": (self.usage_skill1, self.skill1_show),
                "2": (self.usage_skill2, self.skill2_show),
                "3": (self.usage_skill3, self.skill3_show)
            }

        if user_ans in input_mapping:
            usage_skill, skill_show = input_mapping[user_ans]
            if usage_skill == 1:
                if user_ans == "1":
                    self.usage_skill1 = 0
                elif user_ans == "2":
                    self.usage_skill2 = 0
                elif user_ans == "3":
                    self.usage_skill3 = 0

                if skill_show == "Healstream Surge":
                    if self.hearts < 3:
                        self.hearts += 1
                        self.status = "Healstream Surge used to heal 1 heart"
                    else:
                        self.status = "Healstream Surge was wasted"
                elif skill_show == "Quantum Leap":
                    self.points += 1
                    self.status = "Quantum Leap used to gain 1 point"
                    clear()
                    self.start_quiz()
                elif skill_show == "Intuition Insight":
                    for key, value in choices_dict.items():
                        if value == answer:
                            ans_letter = key
                            break

                    keys = list(choices_dict.keys())
                    keys.remove(ans_letter)
                        
                    for key in sample(keys, 2):
                        choices_dict[key] = ""
                elif skill_show == "Resilient Echo":
                    if self.hearts <= 0:
                        self.resilient_checker = True
                        self.status = "Resilient Echo is activated"
                    else:
                        self.status = "Resilient Echo is wasted"
                elif skill_show == "Skill Resurgence":
                    if self.skill1_show == "Skill Resurgence":
                        if self.usage_skill2 == 0 and self.usage_skill3 == 0:
                            self.usage_skill2 = 1
                            self.usage_skill3 = 1
                            self.usage_skill1 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill2_show} and {self.skill3_show}"
                            
                        elif self.usage_skill3 == 0:
                            self.usage_skill3 = 1
                            self.usage_skill1 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill3_show}"
                        elif self.usage_skill2 == 0:
                            self.usage_skill2 = 1
                            self.usage_skill1 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill2_show}"
                        elif self.usage_skill2 != 0 and self.usage_skill3 != 0:
                            self.status = "You wasted Skill Resurgence"
                    elif self.skill2_show == "Skill Resurgence":
                        if self.usage_skill1 == 0 and self.usage_skill3 == 0:
                            self.usage_skill1 = 1
                            self.usage_skill3 = 1
                            self.usage_skill2 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill1_show} and {self.skill3_show}"
                        elif self.usage_skill3 == 0:
                            self.usage_skill3 = 1
                            self.usage_skill2 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill3_show}"
                        elif self.usage_skill1 == 0:
                            self.usage_skill1 = 1
                            self.usage_skill2 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill1_show}"
                        elif self.usage_skill1 != 0 and self.usage_skill3 != 0:
                            self.status = "You wasted Skill Resurgence"
                    elif self.skill3_show == "Skill Resurgence":
                        if self.usage_skill1 == 0 and self.usage_skill2 == 0:
                            self.usage_skill1 = 1
                            self.usage_skill2 = 1
                            self.usage_skill3 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill1_show} and {self.skill2_show}"
                        elif self.usage_skill2 == 0:
                            self.usage_skill2 = 1
                            self.usage_skill3 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill2_show}"
                        elif self.usage_skill1 == 0:
                            self.usage_skill1 = 1
                            self.usage_skill3 = 0
                            self.status = f"Skill Resurgence used to reset {self.skill1_show}"
                        elif self.usage_skill1 != 0 and self.usage_skill2 != 0:
                            self.status = "You wasted Skill Resurgence"
                clear()
            else:
                self.status = f"{skill_show} is currently unavailable"
            self.update_quiz(question, answer, choices_dict)
        else:
            if choices_dict[user_ans] == answer:
                if self.refinement_checker:
                    self.points += 3
                    self.status = "Risky Refinement gives more points!"
                else:
                    self.points += 1
                    self.status = "Correct answer!"
                    if self.vitality_checker:
                        self.vitality_counter += 1
                        if self.vitality_counter == 2 and self.hearts < 3:
                            self.hearts += 1
                            self.status = "Vitality Cascade passive activated!" 
                        elif self.vitality_counter == 2 and self.hearts == 3:
                            self.status = "Hearts is still full!"   
                clear()     
            else:
                if self.hearts == 0:
                    if self.resilient_checker:
                        self.hearts = 1
                        self.status = "Resilient Echo was used to revive you"
                    else:
                        self.end_page()
                    clear()
                else:
                    if self.vitality_checker:
                        self.vitality_counter = 0
                        self.hearts -= 1
                        self.status = "Incorrect answer"
                    elif self.aegis_checker and self.passive == "Aegis Flux":
                        self.status = "Aegis Flux was active!"
                        self.analyze_passive(self.passive)
                    elif not self.aegis_checker and self.passive == "Aegis Flux":
                        self.hearts -= 1
                        self.status = "Aegis Flux was not active!"
                        self.analyze_passive(self.passive)
                    elif self.refinement_checker == True:
                        self.hearts -= 1.5
                        self.status = "Received more damage due to Risky Refinement"
                    else:
                        self.hearts -= 1
                        self.status = "Incorrect answer"
                    clear()


    def end_page(self):
        clear()
        print("Game Over")
        print(f"Final Score: {self.points}")
        print(f"Passive: {self.passive}")
        print("Skills: ")
        print(self.skill1_show)
        print(self.skill2_show)
        print(self.skill3_show)

        back = input("Press B to go back to home: ")
        return back
