dream_vacations = {}

poll_dream_vacation = True

while poll_dream_vacation:

    name = input("Enter your name: ")
    dream_vacation = input("Enter your Dream Vacation: ")

    dream_vacations[name] = dream_vacation

    add = input("Do you want to add again? ")
    if add == "no":
        poll_dream_vacation = False

for name, dream_vacation in dream_vacations.items():
    print(f"{name} wants to go to {dream_vacation}") 