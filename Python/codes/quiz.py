import os
import re
from clr import clear

def quiz():

    global score
    score = 0

    print("--- Quiz ---")

    print("\n1. What year was the very first model of the iPhone released?")
    ans = input("Answer: ").lower()
    if ans == "2007":
        score += 1
        pass

    print("\n2. What's the shortcut for the “copy” function on most computers?")
    ans = input("Answer: ").lower()
    if ans == "ctrl+c" or ans == "ctrl c":
        score += 1
        pass

    print("\n3. What is often seen as the smallest unit of memory?")
    ans = input("Answer: ").lower()
    if ans == "kilobyte":
        score += 1
        pass

    print("\n4. Is Java a type of OS? (yes/no)")
    ans = input("Answer: ").lower()
    if ans == "no":
        score += 1
        pass

    print("\n5. Who is often called the father of the computer?")
    ans = input("Answer: ").lower()
    if ans == "charles babbage":
        score += 1
        pass

    print("\n6. What does “HTTP” stand for?")
    ans = input("Answer: ").lower()
    if ans == "hypertext transfer protocol":
        score += 1
        pass

    print("\n7. Who's Facebook Founder?")
    ans = input("Answer: ").lower()
    if ans == "mark zuckerberg":
        score += 1
        pass

    print("\n8. Which email service is owned by Microsoft?")
    ans = input("Answer: ").lower()
    if ans == "hotmail":
        score += 1
        pass

    print("\n9. Google Chrome, Safari, Firefox, and Explorer are different types of what?")
    ans = input("Answer: ").lower()
    if ans == "web browsers" or ans == "browser":
        score += 1
        pass

    print("\n10. What was Twitter's original name?")
    ans = input("Answer: ").lower()
    if ans == "twttr":
        score += 1
    with open("score.txt", "a") as file:
        file.write(f"Score: {score}\n")

    print(f"\nYour total score is {score}.")
    input("\n\nPress Enter to go back.")


while True:

    clear()

    print("--- Quiz ---")
    print("1. Start ")
    print("2. View Scores ")
    print("3. Exit ")
    print("------------")
    chs = input(">> ")

    if chs == '1':
        clear()
        quiz()

    if chs == '2':
        clear()
        with open("score.txt", "r") as file:

            print(file.read())

            input("Press Enter to go back.")

    if chs == '3':
        break
