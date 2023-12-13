import numpy  
import collections
file = open("input", "r")

#part 1
'''sample = file.readline()
load = []
total = 0
while sample:
    if sample!='\n':
        load.append(list(sample.strip()))
    else:
        saved = total
        for i in range(0, len(load)+1):   #rows check
            try:
                if load[i]==load[i+1] and "#" in load[i]:  
                    mirrored = True
                    try:    
                        for j in range(1, i+1):
                            if (load[i+1+j]==load[i-j]):
                                mirrored=True
                            else:
                                mirrored = False
                                break
                    except:
                        pass
                    if mirrored==True:
                            total+=(i+1)*100
                            break
            except:
                pass
        if not (total!=saved):   #assuming every map has EITHER a vertical or horizontal, not both
            trns = numpy.transpose(load).tolist()
            for i in range(0, len(trns)+1):   #column check
                try:
                    if trns[i]==trns[i+1] and "#" in trns[i]:
                        mirrored = True
                        try:
                            for j in range(1, i+1):
                                    if (trns[i+1+j]==trns[i-j]):
                                        mirrored=True
                                    else:
                                        mirrored = False
                                        break
                        except:
                            pass
                        if mirrored==True:
                            total+=(i+1)
                            break
                except:
                    pass
        load = []
    sample = file.readline()
print(total)'''



#part 2
sample = file.readline()
load = []
total = 0
while sample:
    if sample!='\n':
        load.append(list(sample.strip()))
    else:
        smudgerepair = False
        saved = total
        for i in range(0, len(load)+1):   #rows check
            try:
                count = collections.Counter(numpy.array(load[i]) == numpy.array(load[i+1]))[False]
                if count <= 1:  
                    if count==1: 
                        smudgerepair=True
                    mirrored = True
                    try:   
                        for j in range(1, i+1):
                            if (load[i+1+j]==load[i-j]):
                                mirrored=True
                            else:
                                counter = collections.Counter(numpy.array(load[i+1+j]) == numpy.array(load[i-j]))[False]
                                if counter > 1:
                                    mirrored = False
                                    smudgerepair = False
                                    break
                                else:
                                    smudgerepair=True
                                    pass
                    except:
                        pass
                    if mirrored==True and smudgerepair==True:
                            total+=(i+1)*100
                            break
            except:
                pass
        if not (total!=saved):   #assuming every map has EITHER a vertical or horizontal, not both
            trns = numpy.transpose(load).tolist()
            for i in range(0, len(trns)+1):   #column check
                try:
                    count = collections.Counter(numpy.array(trns[i]) == numpy.array(trns[i+1]))[False]
                    if count==1: 
                        smudgerepair=True
                    if count<=1:
                        mirrored = True
                        try:
                            for j in range(1, i+1):
                                if (trns[i+1+j]==trns[i-j]):
                                    mirrored=True
                                else:
                                    counter = collections.Counter(numpy.array(trns[i+1+j]) == numpy.array(trns[i-j]))[False]
                                    if counter > 1:
                                        mirrored = False
                                        smudgerepair = False
                                        break
                                    else:
                                        smudgerepair=True
                                        pass
                        except:
                            pass
                        if mirrored==True and smudgerepair==True:
                            total+=(i+1)
                            break
                except:
                    pass
        load = []
    sample = file.readline()
print(total)