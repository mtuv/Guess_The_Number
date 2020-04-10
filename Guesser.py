import random


def main():
    print("I am thinking of a number from 0 to 20."
          " What number am I thinking of?")

    com_num = random.randint(0, 20)

    player_num = int(input("Your guess: "))

    while True:
        if player_num == com_num:
            print("You are right. I was thinking of " + str(com_num))
            break
        if player_num > com_num:
            print("Your number is too high.")
            player_num = int(input("Your guess: "))
        if player_num < com_num:
            print("Your number is too low.")
            player_num = int(input("Your guess: "))
    return


main()
