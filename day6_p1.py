import math
def in_bounds(g,height,width):
    if (g[0] < height) and (g[1] < width):
       return True
    else:
       return False




#with open("test.txt", "r") as file:
with open("input_day6_p1.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

height = len(input_data)
width = len(input_data[0])
traveled = []
directions = [(-1,0),(0,1),(1,0),(0,-1)];
#find guard
for i in range(height):
    for j in range(width):
        if input_data[i][j] == "^":
           guard = (i,j)
dir = 0

while(in_bounds(guard,height,width)):
    if not (guard in traveled):
        traveled.append(guard)
    moved = False
    while(not moved):
        i = guard[0] + directions[dir][0]
        j = guard[1] + directions[dir][1]
        if in_bounds((i,j),height,width):        
            if input_data[i][j] == "#":
                    dir = (dir + 1)%4
            else:
                guard = (i,j)
                moved = True
        else:
           guard = (i,j)
           moved=True

print(len(traveled))
