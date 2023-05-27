import msvcrt
import os
 
sdg = 1
description = "No Poverty"
sdg_names = {1: "No Poverty", 2: "Zero Hunger", 3: "Good Health and Well-being", 4: "Quality Education",
    5: "Gender Equality", 6: "Clean Water and Sanitation", 7: "Affordable and Clean Energy",
    8: "Decent Work and Economic Growth", 9: "Industry, Innovation, and Infrastructure", 10: "Reduced Inequality",
    11: "Sustainable Cities and Communities", 12: "Responsible Consumption and Production", 13: "Climate Action",
    14: "Life Below Water", 15: "Life on Land", 16: "Peace, Justice, and Strong Institutions",
    17: "Partnerships for the Goals"}

difficulty = ""
easy = "> Easy"
average = "Average"
hard = "Hard"

def show_level():
    os.system("cls")
    print("QUANTUM CHASE")
    print(f" < SDG {sdg} > ", flush=True)

    print(f" < {description} > ", flush=True)

    sdg_choosing()
    return sdg, description

def show_difficulty():
    global difficulty
    global easy, average, hard
    os.system("cls")
    print(f"SDG {sdg}")
    print("Select Difficulty:")
    
    print(easy)
    print(average)
    print(hard)

    difficulty = "Easy"
    key = msvcrt.getch()
    if key == b'\xe0':  # Check for extended key
        key = msvcrt.getch()
        if key == b'H':
            if easy == "> Easy":
                easy = "Easy"
                average = "Average"
                hard = "> Hard"
                difficulty = "Hard"
            elif average == "> Average":
                easy = "> Easy"
                average = "Average"
                hard = "Hard"
                difficulty = "Easy"
            elif hard == "> Hard":
                easy = "Easy"
                average = "> Average"
                hard = "Hard"
                difficulty = "Average"
            show_difficulty() 
        elif key == b'P':
            if easy == "> Easy":
                easy = "Easy"
                average = "> Average"
                hard = "Hard"
                difficulty = "Average"
            elif average == "> Average":
                easy = "Easy"
                average = "Average"
                hard = "> Hard" 
                difficulty = "Hard"
            elif hard == "> Hard":
                easy = "> Easy"
                average = "Average"
                hard = "Hard"
                difficulty = "Easy"
            show_difficulty()
    return difficulty


def sdg_choosing():
    global sdg
    global description
    key = msvcrt.getch()
    if key == b'\xe0':  # Check for extended key
        key = msvcrt.getch()
        if key == b'K':  # Check for left arrow key
            sdg -= 1
            if sdg == 0:
                sdg = 17
            description = sdg_names[sdg]
            show_level()
        elif key == b'M':
            sdg += 1
            if sdg == 18:
                sdg = 1
            description = sdg_names[sdg]
            show_level()
        elif key == b'\r':
            return sdg, description
