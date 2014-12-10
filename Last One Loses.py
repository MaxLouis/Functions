#Max Louis
#Last One Loses
#04/12/14

print("       ____   ___  _____     ____          ___     ___ _____  ____          __   _____          ____            ")
print("|     |    | /       |      |    | |\   | |       /      |   |    | |\   | |  \    |   |\   |  /                               ")
print("|     |____| \__     |      |    | | \  | |__     \__    |   |____| | \  | |   \   |   | \  | |   ___                          ")
print("|     |    |    \    |      |    | |  \ | |          \   |   |    | |  \ | |   /   |   |  \ | |    |                         ")
print("|___  |    | ___/    |      |____| |   \| |___    ___/   |   |    | |   \| |__/  __|__ |   \|  \___|                                 ")

print()
print()
print()
print()

input("Press Enter to continue...")

print()
print()
print()

import random
import time

pile = random.randrange(1,30)

print("This Pile contains an unkown amount of counters. Take turns to remove counters or play vs AI.")

print()

time.sleep(3)

game_type = int(input("Would you like to play Solo(1) OR 2 Player(2)"))

if game_type == 1:
    print()
    print()
    print("\\Single Player//")

