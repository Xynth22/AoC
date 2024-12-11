import re

# read input_data from file
with open("input_day3_p1.txt", "r") as file:
#with open("test.txt", "r") as file:
  input_data = file.readlines()
thesum = 0
#print(input_data[0])
#commands = re.findall("mul[(]\d+,\d+[)]",input_data[0])
#print(commands)

for line in input_data:
  
    
    commands = []
    enable = True
    eol = False
    
    while(not eol):
    
        if(enable):
            x = re.search("don't\(\)",line)
            if(x):
                parse = slice(0,x.start())            
                news = re.findall("mul\(\d+,\d+\)",line[parse])
                commands.append(news)
                enable = False
                parse = slice(x.end(),len(line))            
                line = line[parse]
            else:
                eol = True
                news = re.findall("mul\(\d+,\d+\)",line)
                commands.append(news)
        else:
            x = re.search("do\(\)",line)
            if(x):
                enable = True
                parse = slice(x.end(),len(line))            
                line = line[parse]
            else:
                eol = True
    #sett = re.findall("mul[(]\d+,\d+[)]",line)        
            
 
  # commands = re.findall("mul[(]\d+,\d+[)]",line)
    for sett in commands:
       for mul in sett:
          factors = re.findall("\d+",mul)
          thesum += int(factors[0]) * int(factors[1])

print("Sum is ",thesum)