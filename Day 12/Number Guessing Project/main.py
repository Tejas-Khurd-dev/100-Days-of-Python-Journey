import random
import art


def taking_input():
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("🤔 I am thinking of a number between 1 to 100")
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        difficulty = input("Choose difficulty: Type 'easy' 😎 or 'hard' 💀: ").lower()
        if difficulty == "easy":
            attempts = 10
            print("😌 You have 10 attempts! Good luck 🍀")
            break
        elif difficulty == "hard":
            attempts = 5
            print("😱 You have only 5 attempts! Be careful ⚡")
            break
        else:
            print("❌ Invalid Input")
            continue

    return random_number, attempts


def play_game():
    print(art.logo)
    random_number, attempts = taking_input()
    while True:
        if attempts < 1:
            print("💀 All attempts are used, You Lose ❌")
            return None

        user_input_number = int(input("👉 Guess a number: "))
        if user_input_number > random_number:
            print("⬆️ Entered number is too high 📈")
            attempts -= 1
            print(f"⏳ {attempts} attempts left")
        elif user_input_number < random_number:
            print("⬇️ Entered number is too low 📉", end = " ")
            attempts -= 1
            print(f"⏳ {attempts} attempts left")
        elif user_input_number == random_number:
            print("🎉✨ You made a correct guess! 🏆🎯")
            return None
        else:
            print("⚠️ Invalid Input")


def start():
    while True:
        play_game()
        again = input("🔁 Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! See you next time 🎯")
            break


start()
