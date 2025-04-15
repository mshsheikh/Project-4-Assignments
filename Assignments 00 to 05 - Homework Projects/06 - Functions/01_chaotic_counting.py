print("\n-- -- -- -- -- -- -- -- -- -- --")
print("   05 - LOOPS & CONTROL FLOW      ")
print("        Chaotic Counting          ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

import random

DL = 0.2    # DL means "done likelihood"

def done():
    return random.random() < DL

def c_c():    # c_c means "chaotic count"

    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for X in range(1, 11):
        if done():
            return
        print(X)
    
def main():
    c_c()
    print("I'm done.")

if __name__ == "__main__":
    main()

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
