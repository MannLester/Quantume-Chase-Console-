import os
import json

from pages import *


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class User:

    def __init__(self):
        self.USER_DATABASE = "user_data/users.json"
        self.username = ""
        self.password = ""
        self.verify_password = ""

    def login(self):
        print("LOG IN\n")
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.validate_login()

    def validate_login(self):
        with open(self.USER_DATABASE, 'r') as f:
            users = json.load(f)

        user_found = False
        password_correct = False

        for user in users:
            if self.username == user["username"]:
                user_found = True
                if self.password == user["password"]:
                    password_correct = True
                    break

        if not user_found:
            clear()
            print("User not found.\n")
            return self.login()

        if not password_correct:
            clear()
            print("Incorrect password.\n")
            return self.login()

    def register(self):
        print("REGISTER\n")
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.verify_password = input("Verify Password: ")
        self.validate_register()

    def validate_register(self):
        with open(self.USER_DATABASE, 'r') as f:
            users = json.load(f)

        for user in users:
            if self.username == user["username"]:
                clear()
                print("Username already taken.\n")
                return self.register()

        if not (8 <= len(self.password) <= 16):
            clear()
            print("Password must be between 8 and 16 characters.\n")
            return self.register()

        if self.password != self.verify_password:
            clear()
            print("Passwords do not match.\n")
            return self.register()
        else:
            users.append({'username': self.username, 'password': self.password})
            with open(self.USER_DATABASE, 'w') as f:
                json.dump(users, f, indent=4)
            clear()
            print("Registered successfully.\n")
            return self.login()

    def get_username(self):
        return self.username

    def change_username(self):
        clear()
        print("CHANGE USERNAME\n")
        username = input("Enter a username: ")

        with open(self.USER_DATABASE, 'r') as f:
            users = json.load(f)

        for user in users:
            if username == user["username"]:
                clear()
                print("Username already taken.\n")
                return self.change_username()

        for user in users:
            if user["username"] == self.username:
                user["username"] = username

        with open(self.USER_DATABASE, 'w') as f:
            json.dump(users, f, indent=4)

        clear()
        print("Username has been changed successfully.\n")

    def change_pass(self):
        clear()
        print("CHANGE PASSWORD\n")
        password = input("Enter a new password: ")

        with open(self.USER_DATABASE, 'r') as f:
            users = json.load(f)

        for user in users:
            if user["username"] == self.username:
                user["password"] = password

        with open(self.USER_DATABASE, 'w') as f:
            json.dump(users, f, indent=4)
        
        clear()
        print("Password has been changed successfully\n")