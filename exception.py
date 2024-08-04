passw = 0
while passw == 0 :
    try:
        passw = int(input("enter your password:"))

    except ValueError:
        print("Error the value must be in digits")
