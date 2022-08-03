import random

hard = 5
easy = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
comp_choice = random.randint(1, 100)
print(f"Tssss comp choice is {comp_choice}")

chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")


def game(level):
    if user_choice < comp_choice:
        print("Your choise is less than computer's choice")
        return level - 1
    if user_choice > comp_choice:
        print("Your choise is more than computer's choice")
        return level - 1


should_continue = True

while should_continue:
    if chosen_difficulty == "easy":
        print(f"You have {easy} attempts remaining to guess the number.")
        user_choice = int(input("Chose your number "))
        if user_choice == comp_choice:
            should_continue = False
            print("you win")
        if user_choice != comp_choice:
            easy = game(easy)
            if easy < 1:
                should_continue = False
                print("game over")
    if chosen_difficulty == "hard":
        print(f"You have {hard} attempts remaining to guess the number.")
        user_choice = int(input("Chose your number "))
        if user_choice == comp_choice:
            should_continue = False
            print("you win")
        if user_choice != comp_choice:
            hard = game(hard)
            if hard < 1:
                should_continue = False
                print("game over")






