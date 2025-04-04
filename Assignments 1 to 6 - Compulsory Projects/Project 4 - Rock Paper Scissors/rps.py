import random

print("\n-- -- -- -- -- -- -- -- -- -- -- -- --")
print("         ROCK PAPER SCISSORS           ")
print(" Play with the computer and have fun!   ")
print("-- -- -- -- -- -- -- -- -- -- -- -- --\n")

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

## print(computer_choice)  # (CHEAT CODE) #

user_choice = input("""✊ Rock
✋ Paper
✌️  Scissors\n
Enter your choice: """).lower()

print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

if user_choice == computer_choice:
    print("It's a tie!")
    
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!\n")
    
else:
    print("You lose!\n")

footer_A : str = "\nMade with ❤️  just for you!"
footer_B : str = "by Muhammad Salman Hussain\n"

print(footer_A)
print(footer_B)
