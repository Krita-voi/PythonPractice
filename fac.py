num=int(input("Enter a number "))
def fact(num):
    if num <= 1 :
        return 1
    else:
        num = num * fact (num-1)
        return num
print("the fact of " ,num, "is",fact(num))


    