import math
def in_bounds(g,height,width):
    if (g[0] >= 0 and g[0] < height) and (g[1] >= 0 and g[1] < width):
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
           guardInit = (i,j)
count = 0
for x in range(height):
    for y in range(width):
        if(input_data[x][y] == "#"): #already blocked
            guard = (height,width)
        else:        
            guard = guardInit
        dir = 0
        steps = 0
        while(in_bounds(guard,height,width)):
            #if not (guard in traveled):
               # traveled.append(guard)
            moved = False
            while(not moved):
                i = guard[0] + directions[dir][0]
                j = guard[1] + directions[dir][1]
                if in_bounds((i,j),height,width) and steps < 10000:        
                    if (input_data[i][j] == "#") or ((i,j)==(x,y)):
                            dir = (dir + 1)%4
                    else:
                        guard = (i,j)
                        steps += 1
                        moved = True
                else:
                    if steps >= 10000:
                        count = count + 1
                        guard = (height,width)
                    else:
                        guard = (i,j)
                    moved=True
         

print(len(traveled))
#print(steps)
print(count)