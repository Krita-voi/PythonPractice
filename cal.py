#run until user says exit 
#user has 4 choise add,sub,multi and div
while True:
    choice = input("give me a operator or exit")
     
    if choice =="exit":
        break

    a =float(input("enter a number: "))
    b =float(input("enter a number: " ))

    if choice=="+":
        print(a+b)

    elif choice=="-":
        print(a-b)

    elif choice=="*":
        print(a*b)

    elif choice =="%":
        print(a%b)
    
    else:
        print("invalid ")
