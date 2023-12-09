file = open("input", "r")
line = list(map(int,file.readline().split()))

#part 1
'''def recurse(nums):  
        return 0
    else:
        newl=[]
        for i in range(1, len(nums)):
            newl.append(nums[i] - nums[i-1])
        return nums[0]+recurse(newl)'''

#part 2
def recurse(nums): 
    if all(num==0 for num in nums):
        return 0
    else:
        newl=[]
        for i in range(1, len(nums)):
            newl.append(nums[i] - nums[i-1])
        return nums[0]-recurse(newl)    #literally just a single sign change

total=0
while line:
    total+=recurse(line)
    line = list(map(int,file.readline().split()))
print(total)