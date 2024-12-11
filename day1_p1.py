# read input_data from file
with open("input_day1_p1.txt", "r") as file:
  input_data = file.readlines()

# columns to lists
a = []
b = []
for line in input_data:
  a.append(int(line.split()[0].strip()))
  b.append(int(line.split()[1].strip()))

a.sort()
b.sort()

dist = 0
simal = 0

for i in range(0,len(a)):
    dist += abs(a[i] - b[i])
    simal += a[i] * b.count(a[i])
    
print("Distance is: ",dist)
print("\nSimalarity is: ",simal)


