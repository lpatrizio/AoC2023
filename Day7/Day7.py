import collections, time
timestart = time.time()
read = open("input", "r")

hands = read.read().split()
cards = []
#part 1
def replace(n):
    if n=="A":
        return 14
    elif n=="K":
        return 13
    elif n=="Q":
        return 12
    elif n=="J":
        return 0
    elif n=="T":
        return 10
    else:
        return n
    

'''for i in range(0, len(hands), 2):
    common = collections.Counter(hands[i]).most_common(2)
    if common[0][1]==5:
        cards.append([7, hands[i], hands[i+1]])
    elif common[0][1]==4:
        cards.append([6, hands[i], hands[i+1]])
    elif common[0][1]==3 and common[1][1]==2:
        cards.append([5, hands[i], hands[i+1]])
    elif common[0][1]==3:
        cards.append([4, hands[i], hands[i+1]])
    elif common[0][1]==2 and common[1][1]==2:
        cards.append([3, hands[i], hands[i+1]])
    elif common[0][1]==2:
        cards.append([2, hands[i], hands[i+1]])
    else:
        cards.append([1, hands[i], hands[i+1]])
       
cards.sort()
swapping = False

while swapping==False:
    swapping=True
    for i in range(0, len(cards)):    
        try:
            if cards[i][0]==cards[i+1][0]:
                temp = list(map(replace,cards[i][1]))
                temp2 = list(map(replace,cards[i+1][1]))
                for j in range(0,5):   
                    if temp[j] > temp2[j]:
                        store = cards[i+1]
                        cards[i+1] = cards[i]
                        cards[i] = store
                        swapping=False
                        break
                    elif temp[j] < temp2[j]:
                        break
                    else:
                        pass
        except:
            pass

total=0
for i in range(0, len(cards)):
    total+= (i+1)*int(cards[i][2])
print(cards)
print(total)'''

    

'''
if common[0][1]==2 and common[0][0]!="J":
            temp = hands[i].replace("J", common[0][0])
            common = collections.Counter(temp).most_common(2)
        elif common[0][1]==2 and common[0][0]=="J" and common[1][1]==2:
            temp = hands[i].replace("J", common[1][0])
            common = collections.Counter(temp).most_common(2)
        elif common[0][0]=="J" and not common[0][1]==5:
            temp = hands[i].replace("J", common[1][0])
            common = collections.Counter(temp).most_common(2)
        else:
            temp = hands[i].replace("J", common[0][0]) 
            common = collections.Counter(temp).most_common(2)'''

for i in range(0, len(hands), 2):
    common = collections.Counter(hands[i]).most_common(2)
    if "J" in hands[i]:
        if common[0][0]=="J" and common[0][1]==5:
            pass
        elif common[0][0]=="J" and common[0][1]!=5:
            temp = hands[i].replace("J", common[1][0]) 
            common = collections.Counter(temp).most_common(2)
        else:
            temp = hands[i].replace("J", common[0][0]) 
            common = collections.Counter(temp).most_common(2)
    test = hands[i]
    if common[0][1]==5:
        cards.append([7, hands[i], hands[i+1]])
    elif common[0][1]==4:
        cards.append([6, hands[i], hands[i+1]])
    elif common[0][1]==3 and common[1][1]==2:
        cards.append([5, hands[i], hands[i+1]])
    elif common[0][1]==3:
        cards.append([4, hands[i], hands[i+1]])
    elif common[0][1]==2 and common[1][1]==2:
        cards.append([3, hands[i], hands[i+1]])
    elif common[0][1]==2:
        cards.append([2, hands[i], hands[i+1]])
    else:
        cards.append([1, hands[i], hands[i+1]])
       
cards.sort()
swapping = False

while swapping==False:
    swapping=True
    for i in range(0, len(cards)):    
        try:
            if cards[i][0]==cards[i+1][0]:
                temp = list(map(int,list(map(replace,cards[i][1]))))
                temp2 = list(map(int, list(map(replace,cards[i+1][1]))))
                for j in range(0,5):   
                    if temp[j] > temp2[j]:
                        store = cards[i+1]
                        cards[i+1] = cards[i]
                        cards[i] = store
                        swapping=False
                        break
                    elif temp[j] < temp2[j]:
                        break
                    else:
                        pass
        except:
            pass

total=0
for i in range(0, len(cards)):
    total+= (i+1)*int(cards[i][2])
print(time.time()-timestart)
print(total)