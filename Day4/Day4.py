import time
starttime = time.time()

input = open("input", "r")



#part 1

'''total = 0
line = input.readline()
while line:
    linepoints=0
    working = line.split(":")
    working = working[1].split("|")
    winnumbers = working[0].split()
    mynumbers = working[1].split()
    for elem in mynumbers:
        if elem in winnumbers and linepoints!=0:
            linepoints*=2
        elif elem in winnumbers and linepoints==0:
            linepoints=1
    line = input.readline()
    total+=linepoints
print(total)'''


#part 2    
line = input.readline()
winning=[]
position=1
while line:
    matching=0
    working = line.split(":")
    working = working[1].split("|")
    winnumbers = working[0].split()
    mynumbers = working[1].split()
    for elem in mynumbers:
        if elem in winnumbers:
            matching+=1
    winning.append([matching, 1])
    line = input.readline()
    position+=1  
total=0
for pos, elem in enumerate(winning):
    total+=elem[1]
    if elem[0]>0:
        for i in range(1, elem[0]+1):
            winning[i+pos][1]+=elem[1]
print(total)
print((time.time()-starttime)*1000)




