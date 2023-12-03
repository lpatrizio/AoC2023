
# part 1
'''
input = open("input" , "r")
line = input.readline()
sum = 0
current = 0
while line:
    valid = True
    current+=1
    line = line.replace(',', '')
    working = line.split(":")
    working = working[1].split(";")
    working = [i.split() for i in working]
    for set in working:
        for i in range(0, len(set)-1):
            if set[i].isdigit:
                if set[i+1] == 'blue':
                    if int(set[i]) > 14:
                        valid = False
                elif set[i+1] == 'red':
                    if int(set[i]) > 12:
                        valid = False
                elif set[i+1] == 'green':
                    if int(set[i]) > 13:
                        valid = False
    if valid == True:
        sum+=current
    line = input.readline()
print(sum)'''

#part 2
input = open("input" , "r")
line = input.readline()
sum = 0
current = 0
while line:
    minred = 0
    minblue = 0
    mingreen = 0
    line = line.replace(',', '')
    working = line.split(":")
    working = working[1].split(";")
    working = [i.split() for i in working]
    for set in working:
        for i in range(0, len(set)-1):
            if set[i].isdigit:
                if set[i+1] == 'blue':
                    if int(set[i]) > minblue:
                        minblue = int(set[i])
                elif set[i+1] == 'red':
                    if int(set[i]) > minred:
                        minred = int(set[i])
                elif set[i+1] == 'green':
                    if int(set[i]) > mingreen:
                        mingreen = int(set[i])
    sum+= mingreen*minred*minblue
    line = input.readline()
print(sum)