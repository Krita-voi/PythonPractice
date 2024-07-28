import random

def game(n):
    random_gusse =random.randint(1,n)
    gusse = 0
    while gusse != random_gusse :
        gusse=int(input("enter the gusse from 1 to {n} " ))
        if gusse > random_gusse:
            print('the number is high')
        elif gusse < random_gusse:
            print("the number is too low")
        
    print(f'the number you have gussed {gusse}is correct ')


game(int(10))   