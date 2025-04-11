print("\n-- -- -- -- -- -- --")
print("  01 - EXPRESSIONS ")
print("  Seconds in Year   ")
print("-- -- -- -- -- -- --\n")

usr_yrs = int(input("Enter number of years: "))

# We have
D = 365 # days
H = 24 # hours
M = 60 # minutes
S = 60 # seconds
# as constant values

days = usr_yrs * D
hours = days * H
minutes = hours * M
seconds = minutes * S

sec_yrs = D * H * M * S

print(f"""
We have {sec_yrs} in 1 year.

In {usr_yrs} year(s) we have,
{days} days, {hours} hours, {minutes} minutes, {seconds} seconds.
""")

footer_A : str = "\nCoded by Muhammad Salman Hussain\n"
print(footer_A)
