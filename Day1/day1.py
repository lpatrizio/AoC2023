import re

#part 1

read = open("input.txt", "r").read()
input = re.sub('[A-Za-z]', '', read).split()
sum=0
for elem in input:
    sum+=int(elem[0]+elem[len(elem)-1])
print(sum)


#part 2
input = read.replace("one", 'o1ne')
input = input.replace("two", 't2wo')
input = input.replace("three", 't3hree')
input = input.replace("four", 'f4our')
input = input.replace("five", 'f5ive')
input = input.replace("six", 's6ix')
input = input.replace("seven", 's7even')
input = input.replace("eight", 'e8ight')
input = input.replace("nine", 'n9ine')
input = re.sub('[A-Za-z]', '', input).split()
sum=0
for elem in input:
    sum+=int(elem[0]+elem[len(elem)-1])
print(sum)
