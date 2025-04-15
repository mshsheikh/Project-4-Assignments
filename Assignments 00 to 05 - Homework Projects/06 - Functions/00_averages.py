print("\n-- -- -- -- -- -- -- -- -- -- --")
print("   05 - LOOPS & CONTROL FLOW      ")
print("            Average               ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

def calc_avrg(num1, num2):
    """Returns the average of two numbers"""
    return (num1 + num2) / 2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

avrg = calc_avrg(num1, num2)
print(f"The average of {num1} and {num2} is {avrg}")

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
