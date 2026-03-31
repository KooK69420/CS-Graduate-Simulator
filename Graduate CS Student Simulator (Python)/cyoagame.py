player_name = str(input("What is your name? ")).capitalize()
print("")

import time
def print_short_sleep(msg):
    print(msg)
    time.sleep(2.5)

text = open("text.txt", "r")
lines = text.readlines()

time.sleep(1)

print_short_sleep("You are " + player_name + ". You just graduated from your three year BSc Computer Science Degree.")

for line in lines[3:7]:
    print(line, end="\r")
    time.sleep(2.5)

print_short_sleep("Eventually, your parents intervene. \"" + player_name + ", I\'ve had enough!\" they shout.")
print_short_sleep("\"All you do is laze about in your bedroom, leeching off our income like a damm parasite!\"")

print("")
for line in lines[11:26]:
    print(line, end="\r")
    time.sleep(2.5)

import question1