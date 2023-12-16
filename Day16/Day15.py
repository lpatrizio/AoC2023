import time
starttime = time.time()

file = open("sample", "r")

#part 1
#store the coordinates in a list if not already in it, then count the length of the list
'''grid = file.read().split()
test = []
for line in grid:
    test.append(list(line))


cor = []
cordir = []


def traverse(coord, direction): #traverse while adding coordinates, if splitting spawn new instance. go until hitting a "wall" (try/accept)
    while True:
        match direction:
            case ">":
                coord[0]+=1
                if coord[0]>len(grid[0])-1:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], ">"]
                    cordir.append(y)
            case "^":
                coord[1]-=1
                if coord[1]<0:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], "^"]
                    cordir.append(y)
            case "v":
                coord[1]+=1
                if coord[1]>len(grid)-1:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], "v"]
                    cordir.append(y)
            case "<":
                coord[0]-=1
                if coord[0]<0:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], "<"]
                    cordir.append(y)
        test[coord[1]][coord[0]]+=(",")
        match grid[coord[1]][coord[0]]:
            case ".":
                pass
            case "-":
                if direction==">" or direction=="<":
                    pass
                else:
                    traverse([coord[0], coord[1]], ">")
                    direction = "<"
            case "|":
                if direction=="^" or direction=="v":
                    pass
                else:
                    traverse([coord[0], coord[1]], "^")
                    direction = "v"
            case "/":
                match direction:
                    case ">":
                        direction = "^"
                    case "^":
                        direction = ">"
                    case "v":
                        direction = "<"
                    case "<":
                        direction = "v"
            case "\\":
                match direction:
                    case ">":
                        direction = "v"
                    case "^":
                        direction = "<"
                    case "v":
                        direction = ">"
                    case "<":
                        direction = "^"

        

traverse([-1,0], ">")
print(len(cor))'''


#part 2
grid = file.read().split()
cor = []
cordir = []

def traverse(coord, direction): #traverse while adding coordinates, if splitting spawn new instance. go until hitting a "wall" (try/accept)
    while True:
        match direction:
            case ">":
                coord[0]+=1
                if coord[0]>len(grid[0])-1:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], ">"]
                    cordir.append(y)
            case "^":
                coord[1]-=1
                if coord[1]<0:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], "^"]
                    cordir.append(y)
            case "v":
                coord[1]+=1
                if coord[1]>len(grid)-1:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], "v"]
                    cordir.append(y)
            case "<":
                coord[0]-=1
                if coord[0]<0:
                    break
                if [coord, direction] in cordir:
                    break
                if coord not in cor:
                    x = [coord[0], coord[1]]
                    cor.append(x)
                    y = [[coord[0], coord[1]], "<"]
                    cordir.append(y)
        match grid[coord[1]][coord[0]]:
            case ".":
                pass
            case "-":
                if direction==">" or direction=="<":
                    pass
                else:
                    traverse([coord[0], coord[1]], ">")
                    direction = "<"
            case "|":
                if direction=="^" or direction=="v":
                    pass
                else:
                    traverse([coord[0], coord[1]], "^")
                    direction = "v"
            case "/":
                match direction:
                    case ">":
                        direction = "^"
                    case "^":
                        direction = ">"
                    case "v":
                        direction = "<"
                    case "<":
                        direction = "v"
            case "\\":
                match direction:
                    case ">":
                        direction = "v"
                    case "^":
                        direction = "<"
                    case "v":
                        direction = ">"
                    case "<":
                        direction = "^"

points = []   
for i in range(0, len(grid)):
    cor = []
    cordir = []
    traverse([-1,i], ">")
    points.append(len(cor))
    cor = []
    cordir = []
    traverse([len(grid), i], "<")
    points.append(len(cor))
    
for i in range(0, len(grid[i])):
    cor = []
    cordir = []
    traverse([i,-1], "v")
    points.append(len(cor))
    cor = []
    cordir = []
    traverse([i, len(grid[i])], "^")
    points.append(len(cor))
print(sorted(points, reverse=True)[0])
print(time.time()-starttime)