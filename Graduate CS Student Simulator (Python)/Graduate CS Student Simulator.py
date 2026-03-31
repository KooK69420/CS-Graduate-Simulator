print("#########################")
print("# CS Graduate Simulator #")
print("#########################")

import time
text = open("text.txt", "r")
lines = text.readlines()

def print_short_sleep(msg):
    print(msg)
    time.sleep(2.5)

print("Start?")
answer = str(input("Yes or No: ")).capitalize()
#Game Started
if answer == "Yes":
    player_name = str(input("What is your name? ")).capitalize()
    print("")

    time.sleep(1)

    #Intro
    print_short_sleep("You are " + player_name + ". You just graduated from your three year BSc Computer Science Degree.")

    for line in lines[3:7]:
        print(line, end="\r")
        time.sleep(2.5)

    print_short_sleep("Eventually, your parents intervene. \"" + player_name + ", We\'ve had enough!\" they shout.")
    print_short_sleep("\"All you do is laze about in your bedroom, leeching off our income like a damm parasite!\"")

    print("")
    for line in lines[11:26]:
        print(line, end="\r")
        time.sleep(2.5)

        #Question 1
    question1 = 1 or 2
    while question1 == 1 or 2:
        print("")
        for line in lines[27:30]:
            print(line, end="\r")
        question1 = int(input("(Type either 1 or 2): "))
        if question1 == 1:
            print("")
            #Question 2
            question2 = 1 or 2 or 3
            while question2 == 1 or 2 or 3:
                for line in lines[33:37]:
                    print(line, end="\r")
                question2 = int(input("(Type either 1, 2 or 3): "))

                if question2 == 1:
                    print("")
                    #Question 3
                    question3 = 1 or 2 or 3
                    while question3 == 1 or 2 or 3:
                        for line in lines[40:45]:
                            print(line, end="\r")
                        question3 = int(input("(Type either 1, 2 or 3): "))

                        if question3 == 1:
                            print("")
                            for line in lines[48:56]:
                                print(line, end="\r")
                                time.sleep(2.5)
                            input("")
                            break

                        elif question3 == 2:
                            print("")
                            for line in lines[77:94]:
                                print(line, end="\r")
                                time.sleep(2.5)
                            answer = "Yes" or "No"
                            while answer == "Yes" or "No":
                                answer = input("Do you want to continue? (Yes/No)").capitalize
                                if answer == "Yes":
                                    print("")
                                elif answer == "No":
                                    break
                                else:
                                    print("Buh?")
                            break

                        elif question3 == 3:
                            print("")
                            for line in lines[61:75]:
                                print(line, end="\r")
                                time.sleep(2.5)
                            answer = "Yes" or "No"
                            while answer == "Yes" or "No":
                                answer = input("Do you want to continue? (Yes/No)").capitalize
                                if answer == "Yes":
                                    print("")
                                elif answer == "No":
                                    break
                                else:
                                    print("Buh?")
                            break

                        else:
                            print("Buh?")

                    break

                elif question2 == 2:
                    print("")
                    for line in lines[77:94]:
                        print(line, end="\r")
                        time.sleep(2.5)
                    answer = "Yes" or "No"
                    while answer == "Yes" or "No":
                        answer = input("Do you want to continue? (Yes/No)").capitalize
                        if answer == "Yes":
                            print("")
                        elif answer == "No":
                            break
                        else:
                            print("Buh?")
                    break

                elif question2 == 3:
                    print("")
                    for line in lines[97:99]:
                        print(line, end="\r")
                        time.sleep(2.5)
                    print("\n")
                    for line in lines[106:111]:
                        print(line, end="\r")
                        time.sleep(2.5)
                    answer = "Yes" or "No"
                    while answer == "Yes" or "No":
                        answer = input("Do you want to continue? (Yes/No)").capitalize
                        if answer == "Yes":
                            print("")
                        elif answer == "No":
                            break
                        else:
                            print("Buh?")
                    break

                else:
                    print("Buh?")

            break

        elif question1 == 2:
            print("")
            for line in lines[102:111]:
                print(line, end="\r")
                time.sleep(2.5)
            answer = "Yes" or "No"
            while answer == "Yes" or "No":
                answer = input("Do you want to continue? (Yes/No)").capitalize
                if answer == "Yes":
                    print("")
                elif answer == "No":
                    break
                else:
                    print("Buh?")
            break

    else:
            print("Buh?")


#Game not started
elif answer == "No":
    print("Damm you hate me frfr ong ong.")
else:
    print("Buh?")



