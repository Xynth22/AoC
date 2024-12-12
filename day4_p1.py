import re

def getCols(a):
  return list(zip(*a))

def getForwardDiag(a):
    size = len(a)
    diags = []
    i=0
    for j in range(size):
        diag =[]
        diag.append(a[i][j])
        limit = min(size-i,size-j)
        for x in range(1,limit):
            diag.append(a[i+x][j+x])
        diags.append(diag)
    j=0
    for i in range(1,size):
        diag =[]
        diag.append(a[i][j])
        limit = min(size-i,size-j)
        for x in range(1,limit):
            diag.append(a[i+x][j+x])
        diags.append(diag)
    return diags

def getBackDiag(a):
    size  = len(a)
    diags = []
    j=size-1
    for i in range(size):        
        diag =[]
        diag.append(a[i][j])
        limit = min(size-i-1,j)
        for x in range(1,limit+1):
            diag.append(a[i+x][j-x])
        diags.append(diag)
    i=0
    for j in range(size-2,-1,-1): 
        diag = []
        diag.append(a[i][j])
        limit = min(size-i,j+1)
        for x in range(1,limit):
            diag.append(a[i+x][j-x])
        diags.append(diag)

    return diags


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
rows = arr
cols = getCols(arr)
fdiags = getForwardDiag(arr)
bdiags = getBackDiag(arr)

count += count_xmas(rows)
count += count_xmas(cols)
count += count_xmas(fdiags)
count += count_xmas(bdiags)
#2535 too low
print(count)