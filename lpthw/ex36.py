from sys import exit
print("This is my first game which created by me!")

def start():
    print("Now, there are three cards: #1, #2, #3.")
    print("You can choose one of them, and something would be start.")
    print("Please give me your choose.")
    choose = input("> ")
    if choose == "1":
        card1()
    elif choose == "2":
        card2()
    elif choose == "3":
        card3()
    else:
        print("Please give me the right number.")
        start()

school = "NUAA", "UESTC", "TUP"
def card1():
    print("Okey, you have got 635 point in the College Entrance Examination.")
    print("And now, you can choose only one college among {}.".format(school))
    print("Which would you choose?")
    choose = input("> ")
    if choose == "NUAA":
        print("Alright, you give me the most stable choose.")
        print("Congratulations! You become a Nuaaer!")
        print("Now, begin your college life.")
        NUAA()
    elif choose == "UESTC":
        print("""Maybe your point can get UESTC's offer.
        But it just depend on your luck.
        Let's test your luck!""")
        luck = input("> ")
        luck_test()
    elif choose == "TUP":
        death("Are you kiding me? Maybe you should see a doctor!")
    else:
        print("Can't you understand my question?")
        death("Maybe you don't fit to be a college students!")

def card2():
    print("Congratulations! You have girlfrind now!")
    print("""Your best friend invite you play LOL.
    And your girlfriend want you go shopping with her in the same time.
    Which one would you choose? GAME or GF?""")
    choose = input("> ")
    if choose == "GAME":
        death("Your girl friend give you a spank, and you have no girlfriend!")
    elif choose == "GF":
        print("Your GF like a dress very much. But she can't afford it.")
        print("""If you buy it now, you'll lest 50 yuan
        and you have to live for 20 days.""")
        print("Would you buy it now? YSE or NOT.")
        shopping = input("> ")
        if shopping == "YES":
            death("Your head must be hurted!")
        elif shopping == "NOT":
            print("Maybe your GF becoming angry.")
            print("live or death depond on your luck.")
            luck_test()
        else:
            death("I can conmunicate with you for a good way!")
    else:
        death("Can you talk with me in a good way?")

def card3():
    print("You are in a room, and the only door closing!")
    print("There is a riddle and you need to solve it.")
    print("Only give the right answer the door would be open.")
    print("Only 5 chance you can give your answer. Otherwise you'll be death!")
    print("Riddle: What kind of dog doesn't bite or bark?")
    i = 0
    while 1:
        answer = input("> ")
        i += 1
        if answer == "Hot dog":
            print("You're right! Now, you get the freedom!")
            exit(0)
        elif i >= 5:
            death("You are death!")
            exit(0)
        else:
            print(f"You have waste {i} chance.")


def NUAA():
    print("PLAY or STUDY, which would you choose?")
    choose = input("> ")
    if choose == "PLAY":
        death("You may regret your choose!")
    elif choose == "STUDY":
        print("Good job!")
        print("Wish you will get a great return!")

def luck_test():
    print("Let's test you are lucky or not.")
    print("Give me a number in range 0 to 9.")
    number = input("> ")
    if "1" in number or "5" in number:
        print("You are lucky enough!")
    else:
        death("You are not a lucky dog!")


def death(death):
    print(death, "Goodbye!")

start()
