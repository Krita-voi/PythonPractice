import random


def game (u):
    random_gusse = random.randint(1,u)
    gusse = 0
    while gusse != random_gusse:
        gusse=int(input(f"enter your gusse between 1 and {u}"))
        if gusse < random_gusse:
            print("number is too low")

        elif gusse > random_gusse:
            print("number is too high")

    print(f'Congrts! you have gussed the number {random_gusse} correctly ')
game(int(10))

