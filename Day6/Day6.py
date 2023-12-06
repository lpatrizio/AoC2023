import time  
starttime = time.time()

input = open("input","r")

#part 1 and part 2
mil = list(map(int, input.readline().split(":")[1].split()))
dist = list(map(int, input.readline().split(":")[1].split()))
total = 1
for i in range(0, len(mil)):
    curtime = mil[i]
    speed = 0
    totalwins = 0
    while curtime:
        if curtime*speed > dist[i]:
            totalwins+=1
        elif curtime*speed < dist[i] and speed > mil[i]//2:    #if we're past halfway and below the target then there's no point in continuing further
            if totalwins!=0:
                total*=totalwins
            break
        speed+=1
        curtime-=1
print(total)
print((time.time()-starttime))