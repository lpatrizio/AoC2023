import re
import time
starttime = time.time()

file = open("sample", "r")

#Part 1
'''seedline = file.readline()
seeds = seedline.split(":")[1].split()
for i in range(0, len(seeds)):
    seeds[i] = [seeds[i], False]
       #if value is less then or equal to source+range:subtract/add by difference between source and destination.
maps = file.read()
maps = re.sub('[A-Za-z-:]', '', maps)
maps = maps.replace("\n\n", " * ")
maps = maps.split()
iter=0
while iter < len(maps):
    if maps[iter]=="*":
        pass        
        iter+=1
        for i in range(0, len(seeds)):
            seeds[i][1]=False
    else:
        dest=int(maps[iter])
        source=int(maps[iter+1])
        rang=int(maps[iter+2])
        for pos, elem in enumerate(seeds):
            if source+rang>=int(elem[0])>=source and elem[1]==False:
                seeds[pos][0]=int(elem[0])-(source-dest)
                seeds[pos][1]=True
            
        iter+=3
seeds.sort()
print(seeds)'''


#Part 2
seedline = file.readline()
seedpairs = seedline.split(":")[1].split()
seeds = []
for i in range(0, len(seedpairs), 2):
    try:
        for j in range(0, int(seedpairs[i+1])):
            seeds.append([int(seedpairs[i])+j, False])
    except:
        pass 
maps = file.read()
maps = re.sub('[A-Za-z-:]', '', maps)
maps = maps.replace("\n\n", " * ")
maps = maps.split()
iter=0
while iter < len(maps):
    if maps[iter]=="*":
        pass        
        iter+=1
        for i in range(0, len(seeds)):
            seeds[i][1]=False
    else:
        dest=int(maps[iter])
        source=int(maps[iter+1])
        rang=int(maps[iter+2])
        for pos, elem in enumerate(seeds):
            if source+rang>=int(elem[0])>=source and elem[1]==False:
                seeds[pos][0]=int(elem[0])-(source-dest)
                seeds[pos][1]=True
            
        iter+=3
seeds.sort()
print(seeds[0])
print(len(seeds))
print((time.time()-starttime))

