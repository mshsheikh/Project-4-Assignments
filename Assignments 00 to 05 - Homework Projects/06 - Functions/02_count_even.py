print("\n-- -- -- -- -- -- -- -- -- -- --")
print("   05 - LOOPS & CONTROL FLOW      ")
print("           Count Even             ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

def count_even():

    numbers = []

    while True:
        user_input = input("Enter an integer or press enter to stop: ")

        if user_input == "":
            break
        
        try:
            num = int(user_input)
            numbers.append(num)

        except ValueError:
            print("Please enter a valid integer or press enter to stop")
    
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    
    print(f"Number of even numbers: {even_count}")

count_even()

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
