phone = input(" phoen : ")

digits ={
    "1":"One",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"nine",
    "0":"Zero",
}
output =''
for char in phone:
    output += digits.get(char,"!")+" "
print(output)
