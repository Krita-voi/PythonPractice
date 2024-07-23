num=int(input("Enter numb to be par "))
org=num
digit = 0
rev = 0

while num > 0:
    digit = num % 10
    num = num // 10
    rev= (rev*10)+digit
     

if org == rev:
    print("the given num is palindrom number",rev)
    exit(0)

print("the given num isnt palindrom number",rev)
    

