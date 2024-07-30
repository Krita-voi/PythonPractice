def emoji_conv(messg):
    words = messg.split(" ")
    emoji = {
        ":)":"😊",
        ":(":"😔"
    }
    output=""
    for x in words :
        output += emoji.get(x,x) + " "
    return output
messg = input(">")
print(emoji_conv(messg))



