import math

def merge(l,r):
    count=1
    tempr=r
    while tempr>10:
        tempr = tempr/10.0
        count += 1
    return l*pow(10,count)+r





#with open("test.txt", "r") as file:
with open("input_day7_p1.txt", "r") as file:
  input_data = file.readlines()

thesum=0
lineNum = 1
for line in input_data:
    left, right = line.split(": ")
    result = int(left)
    operands = list(map(int, right.split()))
    
    wholeLine = [operands[0]+operands[1],operands[0]*operands[1],merge(operands[0],operands[1])]
    run = wholeLine.copy()
    groups=[]
    groups.append(run)
    x = slice(2,len(operands))
    for num in operands[x]:        
        set=[]
        for val in run:
            set.append((val)*num)
            set.append((val)+num)
            set.append(merge(val,num))
            wholeLine.append((val)*num)
            wholeLine.append((val)+num)
            wholeLine.append(merge(val,num))
        run = set.copy()
        groups.append(run)        
    # print(len(operands))
    # print(len(wholeLine))
    # print(pow(3,len(operands)-1))
    # for set in groups:
    #     print(set)
    #print(wholeLine)   
    if result in wholeLine:
        thesum += result
    for i in range(len(groups)):        
        if len(groups[i]) != pow(3,i+1):
            print("Error: Line",lineNum,"size:",len(groups[i]),"set:",i)   
    lineNum += 1
print(thesum)    
#too low 425283565583384
#low     425283572415824
#        425283570939105
#        425283565583384          
    
      

