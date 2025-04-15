print("\n-- -- -- -- -- -- -- -- -- -- --")
print("   05 - LOOPS & CONTROL FLOW      ")
print("           Fibonacci              ")
print("-- -- -- -- -- -- -- -- -- -- --\n")

max = 10000

previous, current = 0, 1

print(previous, end=' ')

while current < max:
    print(current, end=' ')
    
    next_num = previous + current

    previous, current = current, next_num

print()

footer_A: str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
