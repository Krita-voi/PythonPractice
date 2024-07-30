numbers=[5,2,1,5,3,1,3,4,7,4]
new=[]
for number in numbers:
    if number not in new:
        new.append(number)
        new.sort()
        new.reverse()
print(new)
print(numbers.count())