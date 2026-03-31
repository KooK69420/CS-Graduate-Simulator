text = open("text.txt", "r")
lines = text.readlines()
import time


for line in lines[0:20]:
    print(line, end="\r")
    time.sleep(2.5)

text.close()
