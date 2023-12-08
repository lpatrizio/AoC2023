import math
import time
timestart=time.time()

read = open("input", "r")

#part 1
#use dict. Since all same size we can just grab read[0:2], read[4:6], etc. use first as dict key and next two as dict value
'''path = read.readline().strip()
read.readline()
nodes = {}
line = read.readline()
while line:
    nodes[line[0:3]] = (line[7:10], line[12:15])
    line = read.readline()
current = nodes['AAA']
iter=0
pathlength = 0
while True:
    try:
        direction = path[iter]
    except:
        iter=0
        direction = path[0]
    match direction:
        case "L":
            if current[0]=="ZZZ":
                pathlength+=1
                break
            else:
                current = nodes[current[0]]
                pathlength+=1
        case "R":
            if current[1]=="ZZZ":
                pathlength+=1
                break
            else:
                current = nodes[current[1]]
                pathlength+=1
    iter+=1
print(pathlength)'''


#Part 2
path = read.readline().strip()  
read.readline()
nodes = {}
line = read.readline()
ghost = []
while line:
    nodes[line[0:3]] = (line[7:10], line[12:15])
    if(line[2]=="A"):
        ghost.append(line[0:3])
    line = read.readline()
pathcounts = []
for elem in ghost:
    iter=0
    pathlength=0
    current = nodes[elem]
    while True:
        try:
            direction = path[iter]
        except:
            iter=0
            direction = path[0]
        match direction:
            case "L":
                if current[0][2]=="Z":
                    pathcounts.append(pathlength+1)
                    break
                else:
                    current = nodes[current[0]]
                    pathlength+=1
            case "R":
                if current[1][2]=="Z":
                    pathcounts.append(pathlength+1)
                    break
                else:
                    current = nodes[current[1]]
                    pathlength+=1
        iter+=1
print(math.lcm(*pathcounts))
print(time.time()-timestart)