file = open("input", "r")


#part 1
'''read = file.read().splitlines()
   #save the coordinates of every stone and square. before pushing north check if square. to find the loads just use the y value +1
stonecoord = []
cubecoord = []
for y in range(0, len(read)):
    for x in range(0, len(read[y])):
        if read[y][x]=="O":
            stonecoord.append([x,y])        #we need these mutable so no tuples
        elif read[y][x]=="#":
            cubecoord.append([x,y])

for pos, stone in enumerate(stonecoord):
    while True:
        if [stone[0], stone[1]-1] in cubecoord or stone[1]==0 or [stone[0], stone[1]-1] in stonecoord:
            break
        else:
            stonecoord[pos][1]-=1
total = 0
for stone in stonecoord:
    total+=len(read)-(stone[1])
print(total)'''

#part 2
read = file.read().splitlines()
stonecoord = []
cubecoord = []
for y in range(0, len(read)):
    for x in range(0, len(read[y])):
        if read[y][x]=="O":
            stonecoord.append([x,y])       
        elif read[y][x]=="#":
            cubecoord.append([x,y])
dir = ['N','W','S','E']

def cycle():
    for direction in dir:
        match direction:        
            case "N":
                stonecoord.sort(key=lambda x: x[1])  #to properly iterate we need to start with whichever is closest to the edge, use sort to iterate through closest first
                for pos, stone in enumerate(stonecoord):
                    while True:
                        if [stone[0], stone[1]-1] in cubecoord or stone[1]==0 or [stone[0], stone[1]-1] in stonecoord:
                            break
                        else:
                            stonecoord[pos][1]-=1
            case "S":
                stonecoord.sort(key=lambda x: x[1], reverse=True)
                for pos, stone in enumerate(stonecoord):
                    while True:
                        if [stone[0], stone[1]+1] in cubecoord or stone[1]==len(read)-1 or [stone[0], stone[1]+1] in stonecoord:
                            break
                        else:
                            stonecoord[pos][1]+=1
            case "W":
                stonecoord.sort(key=lambda x: x[0])
                for pos, stone in enumerate(stonecoord):
                    while True:
                        if [stone[0]-1, stone[1]] in cubecoord or stone[0]==0 or [stone[0]-1, stone[1]] in stonecoord:
                            break
                        else:
                            stonecoord[pos][0]-=1
            case "E":
                stonecoord.sort(key=lambda x: x[0], reverse=True)
                for pos, stone in enumerate(stonecoord):
                    while True:
                        if [stone[0]+1, stone[1]] in cubecoord or stone[0]==len(read[0])-1 or [stone[0]+1, stone[1]] in stonecoord:
                            break
                        else:
                            stonecoord[pos][0]+=1
    total = 0


for i in range(0, 1000):
    cycle()
total = 0
for stone in stonecoord:
    total+=len(read)-(stone[1])
print(total)




