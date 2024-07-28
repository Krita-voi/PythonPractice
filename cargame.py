
help_user = '''
star - to start the car 
stop - to stop the car 
quit - to exit  
'''

def car_game():
    user=" "
    while user.lower() != "quit" :
        user = input(" play ").strip().lower()
        if user == "start" :
            print("car started... Ready to go! ")
        elif user == "stop" :
            print("car has stopped ")
        elif user == "help":
            print(help_user)
        elif user == "quit":
            print("exiting the game")
        else :
            print ("i don't understand it ")

car_game()
