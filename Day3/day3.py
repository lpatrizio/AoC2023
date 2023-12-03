
from collections import defaultdict

read = open("input", "r").read().split()
#Part 1

'''for i in range(0, len(read)):
    number = ''
    valid=False
    for j in range(0, len(read[i])):
        if read[i][j].isdigit():
            number+= str(read[i][j])
            if i!=0:    #Mistakes were made
                if (read[i-1][j]!='.') and not read[i-1][j].isdigit():  
                        valid=True
            if i!=len(read)-1:
                if (read[i+1][j]!='.') and not read[i+1][j].isdigit():
                    valid=True
            if j!=0:
                if (read[i][j-1]!='.') and not read[i][j-1].isdigit():
                    valid=True
            if j!=len(read[i])-1:
                if (read[i][j+1]!='.') and not read[i][j+1].isdigit():
                    valid=True
            if j!=0 and i!=0:
                if (read[i-1][j-1]!='.') and not read[i-1][j-1].isdigit():
                    valid=True
            if j!=len(read[i])-1 and i!=len(read)-1:
                if (read[i+1][j+1]!='.') and not read[i+1][j+1].isdigit():
                    valid=True
            if j!=0 and i!=len(read)-1:
                if (read[i+1][j-1]!='.') and not read[i+1][j-1].isdigit():
                    valid=True
            if j!=len(read[i])-1 and i!=0:
                if (read[i-1][j+1]!='.') and not read[i-1][j+1].isdigit():
                    valid=True
        if not read[i][j].isdigit() or j==len(read[i])-1:
                if valid==True:
                    sum+=int(number)
                number=''
                valid=False
print(sum)'''

#Part 2
sum=0
grid = defaultdict(lambda: ".")                                   
for i in range(0, len(read)):
    number = ''
    for j in range(0, len(read[i])):
        if read[i][j].isdigit():
            number+= str(read[i][j])
        if not read[i][j].isdigit() or j==len(read[i])-1:
            for coord in range(0, len(number)):
                grid[(i,j-1-coord)] = number
            number= ''
for i in range(0, len(read)-1):
    ratio = []
    for j in range(0, len(read[i])):
        if not read[i][j].isdigit() and not read[i][j]=='.':
            for x in range(i-1, i+2):
                for y in range(j-1,j+2):
                    if grid[(x,y)].isdigit() and grid[(x,y)] not in ratio:
                        ratio.append(grid[(x,y)])
            if len(ratio)==2:
                sum+=(int(ratio[0])*int(ratio[1]))
            ratio=[]
print(sum)
