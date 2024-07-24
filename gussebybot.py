import random

def game(n):
    low = 1
    high = n
    computer =''
    while computer != "correct":
        if low != high:
            gusse = random.randint(1,n)
        else:
            gusse = low
        computer = input(f"is the number {gusse} too high or too low: ")
        if computer == "high":
            gusse -=1
        elif computer == "low":
            gusse =+1
    print(f"the computer has gussed  your number {gusse}  ")    


game(10)
