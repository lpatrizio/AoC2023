file = open("input", "r")


#part 1
'''total = 0
line = file.read().split(",")
for seq in line:
    current = 0
    for elem in seq:
        current+=ord(elem)
        current*=17
        current = current%256
    total+=current
print(total)'''     #not even 5 min to do thanks eric

#part 2
total = 0
boxes = {}
line = file.read().split(",")
for seq in line:
    current = 0
    label = ''
    for pos, elem in enumerate(seq):
        if elem == "=":
            focal = int(seq[pos+1])
            if current in boxes:
                replace = False
                for pos, lens in enumerate(boxes[current]):
                    if label in lens:
                        boxes[current][pos] = [label, focal]
                        replace = True
                        break
                if replace==False:
                    boxes[current].append([label, focal])
            else:
                boxes[current] = [[label, focal]]
            break
        elif elem == "-":
            if current in boxes:
                for pos, lens in enumerate(boxes[current]):
                    if label in lens:
                        boxes[current].pop(pos)
                        break
            else:
                break
        else:
            current+=ord(elem)
            current*=17
            current = current%256
            label+=elem

for i in range(0, 257):
    if i in boxes:
        for pos, lens in enumerate(boxes[i]):
            total+= (1+i)*(pos+1)*lens[1]
print(total)