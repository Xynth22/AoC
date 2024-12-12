import re

def getCols(a):
  return list(zip(*a))

def checkMAS(a):
    if(re.findall("(?=(MAS)|(SAM))","".join(a))):
        return True
    else:
        return False


def getForwardMAS(a):
    size = len(a)
    MAScoord = []
    i=0
    for j in range(size):
        tester = ['X','X','X']
        tester.pop(0)
        tester.append(a[i][j])
        limit = min(size-i,size-j)
        for x in range(1,limit):
            tester.pop(0)
            tester.append(a[i+x][j+x])
            if checkMAS(tester):
                MAScoord.append((i+x-1,j+x-1)) #grab last coordinates                    
    j=0
    for i in range(1,size):
        tester = ['X','X','X']
        tester.pop(0)
        tester.append(a[i][j])
        limit = min(size-i,size-j)
        for x in range(1,limit):
            tester.pop(0)
            tester.append(a[i+x][j+x])
            if checkMAS(tester):
                MAScoord.append((i+x-1,j+x-1)) #grab last coordinates        
    return MAScoord

def getBackMAS(a):
    size  = len(a)
    MAScoord = []
    j=size-1
    for i in range(size):        
        tester = ['X','X','X']
        tester.pop(0)
        tester.append(a[i][j])
        limit = min(size-i-1,j)
        for x in range(1,limit+1):
            tester.pop(0)
            tester.append(a[i+x][j-x])
            if checkMAS(tester):
                MAScoord.append((i+x-1,j-x+1)) #grab last coordinates
    i=0
    for j in range(size-2,-1,-1): 
        tester = ['X','X','X']
        tester.pop(0)
        tester.append(a[i][j])
        limit = min(size-i,j+1)
        for x in range(1,limit):
            tester.pop(0)
            tester.append(a[i+x][j-x])
            if checkMAS(tester):
                MAScoord.append((i+x-1,j-x+1)) #grab last coordinates
    return MAScoord


def count_xmas(a)    :
    count = 0
    for row in a:
        count += len(re.findall("(?=(XMAS)|(SAMX))","".join(row)))
    return count
    

# read input_data from file
#with open("test.txt", "r") as file:
with open("input_day4_p1.txt", "r") as file:
  input_data = file.readlines()

# split input_data into 2d character array
arr = [list(line.strip()) for line in input_data]
count = 0
#rows = arr
#cols = getCols(arr)
fCoords = getForwardMAS(arr)
bCoords = getBackMAS(arr)

for f in fCoords:
    for b in bCoords:
        if f == b:
            count += 1




#2535 too low
print(count)