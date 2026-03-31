import time
text = open("text.txt", "r")
lines = text.readlines()

question1 = 1 or 2

while question1 == 1 or 2:
    for line in lines[27:30]:
        print(line, end="\r")
    question1 = int(input("(Type either 1 or 2): "))
    if question1 == 1:
        print("")
        import question2
        break

    elif question1 == 2:
        print("")
        for line in lines[102:111]:
            print(line, end="\r")
            time.sleep(2.5)
        break

    else:
        print("Buh?")
