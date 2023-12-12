import collections
file = open("input", "r")

#part 1
'''expanded = []
galaxy = file.readline()
while galaxy:
    if len(collections.Counter(list(*galaxy.split())).most_common())==1:
        expanded.append(list(*galaxy.split()))
    expanded.append(list(*galaxy.split()))
    galaxy = file.readline() 


for i in range(len(expanded[0])-1, -1, -1): #work backwards so we don't trip over our own inserts
    blank = True
    for j in range(0, len(expanded)):
        if expanded[j][i]!='.':
            blank = False
    if blank==True:
        for j in range(0, len(expanded)):
            expanded[j].insert(i, ".")
            blank=False

coords = []
total = 0
for i in range(0, len(expanded)):
    for j in range(0, len(expanded[i])):
        if expanded[i][j]=="#":
            coords.append([i+1,j+1])    #add one because we start at zero
for i in range(0, len(coords)):
    for j in range(i+1, len(coords)):
        total+= abs(coords[i][0]-coords[j][0])+abs(coords[i][1]-coords[j][1])
print(total)'''

#part 2

galaxy = file.readline()
column = []
counter = 0
expanded = []
while galaxy:
    if len(collections.Counter(list(*galaxy.split())).most_common())==1:
        counter+=1000000
        expanded.append(list(*galaxy.split()))
    else:
        counter+=1
        expanded.append(list(*galaxy.split()))
    column.append(counter)
    galaxy = file.readline() 

row = []
counter = 0
for i in range(0, len(expanded[0])): 
    blank = True
    for j in range(0, len(expanded)):
        if expanded[j][i]=="#":
            blank = False
    if blank==True:
        counter+=1000000
    else:
        counter+=1
    row.append(counter)

coords = []
total = 0
for i in range(0, len(expanded)):
    for j in range(0, len(expanded[i])):
        if expanded[i][j]=="#":
            xval = column[i]
            yval = row[j]
            coords.append([xval,yval])

for i in range(0, len(coords)):
    for j in range(i+1, len(coords)):
        total+= abs(coords[i][0]-coords[j][0])+abs(coords[i][1]-coords[j][1])

print(total)



