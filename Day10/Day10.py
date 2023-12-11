file = open("input", "r")

#part 1
'''plot = file.read().split() 
startcoord= ()
for i in range(0, len(plot)):
    if 'S' in plot[i]:
        startcoord= [i, plot[i].index('S')]
runner1 = []
runner2 = [] #horizontal starting runner #rewrite this to be match case and check that current coord is not first runner's coordinate
runners = [runner1, runner2]
for i in range(0, len(runners)):
    print([startcoord[0]+1, startcoord[1], "v"] not in runners)
    if plot[startcoord[0]+1][startcoord[1]] in ['L', 'J', '|']:
        if [startcoord[0]+1, startcoord[1], "v"] not in runners:
            runners[i] = [startcoord[0]+1, startcoord[1], "v"]
    if plot[startcoord[0]-1][startcoord[1]] in ['7', 'F', '|']:
        if [startcoord[0]-1, startcoord[1], "^"] not in runners:
            runners[i] = [startcoord[0]-1, startcoord[1], "^"]
    if plot[startcoord[0]][startcoord[1]+1] in ['7', 'J', '-']:
        if [startcoord[0], startcoord[1]+1, ">"] not in runners:
            runners[i] = [startcoord[0], startcoord[1]+1, ">"]
    if plot[startcoord[0]][startcoord[1]-1] in ['L', 'F', '-']:
        if [startcoord[0], startcoord[1]-1, "<"] not in runners:
            runners[i] = [startcoord[0], startcoord[1]-1, "<"]
length=1
while True: 
    length+=1
    for runner in runners:
        match plot[runner[0]][runner[1]]:
            case "|":
                if runner[2]=="v":
                    runner[0]+=1
                else:
                    runner[0]-=1
            case "-":
                if runner[2]==">":
                    runner[1]+=1
                else:
                    runner[1]-=1
            case "L":
                if runner[2]=="<":
                    runner[0]-=1
                    runner[2]="^"
                else:
                    runner[1]+=1
                    runner[2]=">"
            case "J":
                if runner[2]==">":
                    runner[0]-=1
                    runner[2]="^"
                else:
                    runner[1]-=1
                    runner[2]="<"
            case "7":
                if runner[2]==">":
                    runner[0]+=1
                    runner[2]="v"
                else:
                    runner[1]-=1
                    runner[2]="<"
            case "F":
                if runner[2]=="^":
                    runner[1]+=1
                    runner[2]=">"
                else:
                    runner[0]+=1
                    runner[2]="v"
    

    if runners[0][0]==runners[1][0] and runners[0][1]==runners[1][1]:
        break
print(length)'''

#part 2
plot = file.read().split() 
startcoord= ()
for i in range(0, len(plot)):
    plot[i] = list(plot[i])
    if 'S' in plot[i]:
        startcoord= [i, plot[i].index('S')]
runner = []
if plot[startcoord[0]][startcoord[1]+1] in ['7', 'J', '-']:
        runner = [startcoord[0], startcoord[1]+1, ">"]
        remember = [startcoord[0], startcoord[1]+1, ">"]
elif plot[startcoord[0]+1][startcoord[1]] in ['L', 'J', '|']:
        runner = [startcoord[0]+1, startcoord[1], "v"]
        remember = [startcoord[0]+1, startcoord[1], "v"]
elif plot[startcoord[0]-1][startcoord[1]] in ['7', 'F', '|']:
        runner = [startcoord[0]-1, startcoord[1], "^"]
        remember = [startcoord[0]-1, startcoord[1], "^"]
elif plot[startcoord[0]][startcoord[1]-1] in ['L', 'F', '-']:
        runner = [startcoord[0], startcoord[1]-1, "<"]
        remember = [startcoord[0], startcoord[1]-1, "<"]
length=1
while True: 
    length+=1
    match plot[runner[0]][runner[1]]:
        case "|":
            if runner[2]=="v":
                plot[runner[0]][runner[1]] = 'v'
                runner[0]+=1
            else:
                plot[runner[0]][runner[1]] = '^'
                runner[0]-=1
        case "-":
            if runner[2]==">":
                plot[runner[0]][runner[1]] = '>'
                runner[1]+=1
            else:
                plot[runner[0]][runner[1]] = '<'
                runner[1]-=1
        case "L":
            if runner[2]=="<":
                plot[runner[0]][runner[1]] = 'U'
                runner[0]-=1
                runner[2]="^"
            else:
                plot[runner[0]][runner[1]] = 'U'
                runner[1]+=1
                runner[2]=">"
        case "J":
            if runner[2]==">":
                plot[runner[0]][runner[1]] = 'U'
                runner[0]-=1
                runner[2]="^"
            else:
                plot[runner[0]][runner[1]] = 'U'
                runner[1]-=1
                runner[2]="<"
        case "7":
            if runner[2]==">":
                plot[runner[0]][runner[1]] = 'v'
                runner[0]+=1
                runner[2]="v"
            else:
                plot[runner[0]][runner[1]] = '^'
                runner[1]-=1
                runner[2]="<"
        case "F":
            if runner[2]=="^":
                plot[runner[0]][runner[1]] = '^'
                runner[1]+=1
                runner[2]=">"
            else:
                plot[runner[0]][runner[1]] = 'v'
                runner[0]+=1
                runner[2]="v"
    

    if plot[runner[0]][runner[1]]=="S":
        break

inside = False
counter = 0
newplot = []

for line in plot:
    newline=[]
    for elem in line:
        if (elem=="^" or elem=="v" or elem=="S") and inside==False:
            inside = True
            newline.append("U")
        elif (elem=="^" or elem=="v" or elem=="S") and inside==True:
            inside = False
            newline.append("D")
        elif elem in ["|",".","7","F","-", "J", "L"] and inside==True:
            counter+=1
            newline.append(elem)
        else:
            newline.append(elem)
    inside=False
    newplot.append(newline)
for line in newplot:
    print(*line)
print(counter)
        
        





