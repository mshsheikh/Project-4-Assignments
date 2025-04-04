# Guess The Number (User) - by mshsheikh

import random

print("\n-- -- -- -- -- -- -- -- -- -- -- -- --")
print("           GUESS THE NUMBER         ")
print(" Play with the computer and have fun! ")
print("-- -- -- -- -- -- -- -- -- -- -- -- --\n")

print("""User 👤: I have a number between 1 and 6.
         Let's see if the computer can guess it!""")

low : int = 1
high : int = 6

while True:
  computer_guess = random.randint(low, high)
  print(f"\nBOT 🤖: Is it {computer_guess}?")

  feedback : str = input("\nEnter L if it's too Low, H if it's too High, or C if it's Correct: ").lower()

  if feedback == 'l':
    low = computer_guess + 1
    print("\nBOT 🤖: Hmm... Too low? Let me guess higher.")

  elif feedback == 'h':
    high = computer_guess - 1
    print("\nBOT 🤖: Oh! Too high? I'll try a smaller one.")

  elif feedback == 'c':
    print("\nBOT 🤖: Yay! I guessed it right!")

    break

  else:
    print("Please enter a valid option: L, H, or C.")

footer_A : str = "\nMade with ❤️  just for you!"
footer_B : str = "by Muhammad Salman Hussain\n"

print(footer_A)
print(footer_B)
