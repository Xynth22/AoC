
# read input_data from file
with open("input_day2_p1.txt", "r") as file:
#with open("test.txt", "r") as file:
  input_data = file.readlines()

def check_safety(a):
    change = [0] * (len(a)-1)
    for i in range(0,len(a)-1):
        change[i] = a[i]-a[i+1]
    if(all(x>0 for x in change) or all(x<0 for x in change)):
        if(all(abs(x)<4 for x in change)):
            return True
    #Else
    return False


total = 0

pad_total = 0
for line in input_data:
  nums = [int(num.strip()) for num in line.split()]
  
  if check_safety(nums):
    total += 1
    pad_total += 1
  else:
    pad = False
    for i in range(0,len(nums)):
        temp_nums = nums.copy()
        temp_nums.pop(i)
        if check_safety(temp_nums):
            pad = True
      
    if(pad):
      pad_total += 1


    
print("Safe Lines: ",total)
print("Padded Safe Lines: ",pad_total)
#print("\nSimalarity is: ",simal)


