import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Loadout:
    def __init__(self):
        self.passive_list = {
            "1. Vitality Cascade": "Answering 2 consecutive right answers will heal you by 1",
            "2. Aegis Flux": "At random intervals, the player will receive a shield that nullifies damage from wrong answers",
            "3. Time warp": "Lets you add 5s to the time",
            "4. Unleashed Arsenal": "Can bring 1 more skill to the game",
            "5. Risky Refinement": "Gains more points but also receives more damage"
            
        }

        self.skill_list = {
            "A": "Healstream Surge: Instantly heals you by 1",
            "B": "Quantum Leap: Lets you skip a question",
            "C": "Intuition Insight: Removes 2 non-correct choices",
            "D": "Resilient Echo: Revives the player with one health",
            "E": "Skill Resurgence: Instantly resets your other skills"
        }

        self.skill_counter = 0
        self.num_skills = 2  # Default number of skills
        self.chosen_passive = ""
        self.chosen_skills = []

    def passive_picking(self):
        clear()
        print("L O A D  O U T")
        print("\nPassive:")
        for passive, description in self.passive_list.items():
            print(f"\n   {passive}")
            print(f"      {description}")

        self.chosen_passive = input("\nWhich passive do you choose: ")
        self.skill_picking()

    def skill_picking(self):
        if self.chosen_passive == "4":
            print("\n\nPassive: Unleashed Arsenal is active! Pick 3 skills")
            self.num_skills = 3

        while len(self.chosen_skills) < self.num_skills:
            print(f"\n\nSkill {len(self.chosen_skills) + 1}:\n")

            for key, description in self.skill_list.items():
                if key not in self.chosen_skills:
                    print(f"   {key}. {description}\n")

            skill_choice = input("Which skill do you choose (enter the letter): ").upper()

            if skill_choice in self.skill_list.keys() and skill_choice not in self.chosen_skills:
                self.chosen_skills.append(skill_choice)
                del self.skill_list[skill_choice]
            else:
                print("Error: Invalid skill or skill already chosen. Choose a different skill.")

        return self.chosen_skills

    def start_loadout_selection(self):
        self.passive_picking()

        return self.chosen_passive, self.chosen_skills

loadout = Loadout()
