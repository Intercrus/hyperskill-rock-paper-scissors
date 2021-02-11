from random import choice

options_15 = {
    'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
    'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
}

options_5 = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['lizard', 'paper'],
    'spock': ['scissors', 'rock'],
    'lizard': ['spock', 'paper']
}

params = ['rock', 'paper', 'scissors']

user_name = input("Enter your name: ")

with open(r"rating.txt", "r") as file:
    get_rating_from_file = [line.split() for line in file.readlines()]
    db_rating = {name: int(score) for name, score in get_rating_from_file}

    if user_name not in db_rating:
        db_rating[user_name] = 0

    print(f"Hello, {user_name}")

while True:
    user_params = input("Enter your params: ").split(",")

    if len(user_params) == 1:
        print("Okay, let's start")
        break
    else:
        params = user_params
        print("Okay, let's start")
        break

def lose_or_not(user, machine):
    if len(params) == 3:
        if (user_command == 'rock' and machine_input == 'paper') or \
                (user_command == 'paper' and machine_input == 'scissors') or \
                    (user_command == 'scissors' and machine_input == 'rock'):
            return True
    if len(params) == 5:
        for key, value in options_5.items():
            if (key == user_command) and (machine in options_5[key]):
                return False
            else:
                return True
    if len(params) == 15:
        for key in options_15:
            if (machine == key) and (user in options_15[key]):
                return True
            elif (user == key) and (machine in options_15[key]):
                return False

while True:
    user_command = input()

    if user_command == "!exit":
        print("Bye!")
        break
    elif user_command == '!rating':
        print(f"Your rating: {db_rating[user_name]}")
    elif user_command not in params:
        print("Invalid input")
    else:
        machine_input = choice(params)
        if user_command == machine_input:
            print(f"There is a draw ({machine_input})")
            db_rating[user_name] += 50
        elif lose_or_not(user_command, machine_input):
            print(f"Sorry, but the computer chose {machine_input}")
        else:
            print(f"Well done. The computer chose {machine_input} and failed")
            db_rating[user_name] += 100