age = int(input("Please enter your age: "))
is_citizen = input("Are you a natural born citizen of the U.S (yes/no)? ").lower() == "yes"
years_resided = int(input("How many years have you resided in the U.S.? "))

eligible = True
3
if not is_citizen:
    eligible = False

if age < 35:
    eligible_to_run = False

if years_resided < 14:
    eligible = False

if eligible: 
    print("You can run for president of USA.")
else:
    print("You cannot run for president of USA.")