# Mad Libs Fun - by mshsheikh

def funny_line():
    print("-- -- -- -- -- -- -- -- -- --")
    print("       M A D    L I B S      ")
    print("  Let's create a funny line! ")
    print("-- -- -- -- -- -- -- -- -- --")

    adj = input("Enter an adjective: ").lower()
    noun = input("Enter a noun: ").lower()
    verb = input("Enter a verb: ").lower()
    place = input("Enter a place: ").lower()

    line_1 = f"Today, a {adj} {noun} decided to {verb} all the way to {place}..."

    print("\nYour funny line:")
    print(line_1)

    print("\nMade with ❤️  just for you!")
    print("by Muhammad Salman Hussain\n")

funny_line()
