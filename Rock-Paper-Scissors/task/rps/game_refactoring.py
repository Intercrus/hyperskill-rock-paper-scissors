
from random import choice

user_name, user_rating = input("Enter your name: "), 0
print(f"Hello, {user_name}")

with open(r"rating.txt", "r", encoding="utf-8") as file:
    for line in file:
        user_name_from_file, user_rating_from_file = line.split()

        if user_name_from_file == user_name:
            user_rating = user_rating_from_file
            break

parameters = input("Enter your options: ").split(",")
if parameters == ['']:  # if user press 'Enter'
    parameters = ["rock", "paper", "scissors"]
print("Okay, let's start")

while True:
    user_command = input()

    if user_command == "!exit":
        print("Bye!")
        break
    elif user_command == '!rating':
        print(f"Your rating: {user_rating}")
    elif user_command not in parameters:
        print("Invalid input")
    else:
        machine_choice = choice(parameters)  # random item
        if user_command == machine_choice:
            print(f"There is a draw ({machine_choice})")
            user_rating += 50
        elif (parameters.index(machine_choice)
              - parameters.index(machine_choice)) % len(parameters)  \
              > len(parameters) // 2:
            print(f"Sorry, but the computer chose {machine_choice}")
        else:
            print(f"Well done. The computer chose {machine_choice} and failed")
            user_rating += 100





