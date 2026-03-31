import time

text = open("text.txt", "r")
lines = text.readlines()

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
        break

    elif question3 == 2:
        print("")
        for line in lines[77:94]:
            print(line, end="\r")
            time.sleep(2.5)
        break

    elif question3 == 3:
        print("")
        for line in lines[61:75]:
            print(line, end="\r")
            time.sleep(2.5)
        break

    else:
        print("Buh?")