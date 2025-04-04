# Mad Libs Fun

def create_story():
    print("-- -- -- -- -- -- -- -- -- --")
    print("       M A D   L I B S     ")
    print(" Let's create a funny story!")
    print("-- -- -- -- -- -- -- -- -- --")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    story = f"Today, a {adjective} {noun} decided to {verb} all the way to {place}..."

    print("\nYour Story:")
    print(story)

    print("\nMade with ❤️  just for you!\n")
    print("\nby Muhammad Salman Hussain\n")

create_story()