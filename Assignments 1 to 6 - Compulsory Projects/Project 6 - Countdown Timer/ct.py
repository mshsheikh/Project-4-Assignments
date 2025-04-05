import time

print("\n-- -- -- -- -- -- -- --")
print("    COUNTDOWN TIMER    ")
print("-- -- -- -- -- -- -- -- \n")

user_time = int(input("Enter the time in seconds: "))

while user_time > 0:

    mins = user_time // 60
    secs = user_time % 60

    timer = f"{mins:02d}:{secs:02d}"

    print(timer, end="\r")

    time.sleep(1)

    user_time -= 1

print("⋆ Ｔｉｍｅｒ　Ｃｏｍｐｌｅｔｅｄ! ⋆")

footer_A : str = "\nMade with ❤️  just for you!"
footer_B : str = "by Muhammad Salman Hussain\n"

print(footer_A)
print(footer_B)