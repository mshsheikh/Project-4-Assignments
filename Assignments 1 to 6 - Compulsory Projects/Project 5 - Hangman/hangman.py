import random

print("\n-- -- -- -- -- --")
print("     HANGMAN      " )
print("-- -- -- -- -- --\n")

words = [
    "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon",
    "mango", "orange", "papaya", "raspberry", "strawberry", "ugli", "vanilla",
    "watermelon", "yam", "apricot", "blackberry", "dragonfruit", "eggplant",
    "guava", "jackfruit", "lime", "olive", "peach","avocado", "blueberry",
    "durian", "grapefruit", "pineapple", "tomato", "miracle", "naranjilla",
    "pine", "cocoa", "hazelnut", "almond", "walnut", "pomegranate", "lychee",]

word = random.choice(words)
word = word.upper()

## print(word) # (CHEAT CODE) #

display = " "

for char in word:
    display += "_"

attempts = 6

guessed_letters = " "

# Loop:
while attempts > 0 and display != word:
    
    print("Word:", " ".join(display))
    print("Guessed Letters:", guessed_letters)
    print("Remaining Attempts:", attempts)

    guess = input("\nGuess a letter: ").upper()
    
    # Alphabetical check: -- -- -- -- -- -- -- -- 
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!\n")
        continue
    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        
        continue

    guessed_letters += guess

    if guess in word:
        new_display = " "

        for i in range(len(word)):

            if word[i] == guess:
                new_display += guess

            else:
                new_display += display[i]

        display = new_display
        print("\nGood guess!\n")
  
    else:
        attempts -= 1
        print("\nWrong guess!\n")

if display == word:
    print("Congratulations!", word)

else:
    print("Sorry, you're out of attempts.\nThe word was: ", word.upper())

footer_A : str = "\nMade with ❤️  just for you!"
footer_B : str = "by Muhammad Salman Hussain\n"

print(footer_A)
print(footer_B)
