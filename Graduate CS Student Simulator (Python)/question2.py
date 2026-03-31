import time

text = open("text.txt", "r")
lines = text.readlines()

question2 = 1 or 2 or 3

while question2 == 1 or 2 or 3:
    for line in lines[33:37]:
        print(line, end="\r")
    question2 = int(input("(Type either 1, 2 or 3): "))

    if question2 == 1:
        print("")
        import question3
        break

    elif question2 == 2:
        print("")
        for line in lines[77:94]:
            print(line, end="\r")
            time.sleep(2.5)
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
        break

    else:
        print("Buh?")