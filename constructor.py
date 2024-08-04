class person :
    def __init__(self , name ):
        self.name = name

    def talk(self):
        print (f"Hello! {self.name}")


user = person(input("what is your name: "))
user.talk()

    
