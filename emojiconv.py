messg = input(">")
words = messg.split(" ")
emoji = {
    ":)":"😊",
    ":(":"😔"
}
output=""
for x in words :
    output += emoji.get(x,x) + " "
print(output) 