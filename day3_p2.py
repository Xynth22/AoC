import re

# read input_data from file
with open("input_day3_p1.txt", "r") as file:
#with open("test.txt", "r") as file:
  input_data = file.read()
thesum = 0
theosum = 0
#print(input_data[0])
#commands = re.findall("mul[(]\d+,\d+[)]",input_data[0])
#print(commands)
input_data = re.sub(r"don't\(\).*?(?:do\(\)|$)", "", input_data, flags=re.DOTALL)

commands = re.findall("mul\(\d+,\d+\)",input_data)

# for line in input_data:

    
#     commands = []
#     notCommands = []
#     enable = True
#     eol = False
#     origLine=line
#     while(not eol):
    
#         if(enable):
#             x = re.search("don't\(\)",line)
#             if(x):
#                 parse = slice(0,x.start())            
#                 news = re.findall("mul\(\d+,\d+\)",line[parse])
#                 commands.append(news)
#                 enable = False
#                 parse = slice(x.end(),len(line))            
#                 line = line[parse]
#             else:
#                 eol = True
#                 news = re.findall("mul\(\d+,\d+\)",line)
#                 commands.append(news)
#         else:
#             x = re.search("do\(\)",line)
#             if(x):
#                 #debug
#                 parse = slice(0,x.start())            
#                 news = re.findall("mul\(\d+,\d+\)",line[parse])
#                 notCommands.append(news)
#                 #debug
#                 enable = True
#                 parse = slice(x.end(),len(line))                            
#                 line = line[parse]
#             else:
#                 eol = True
#     #sett = re.findall("mul[(]\d+,\d+[)]",line)        
            
 
#     origCommands = re.findall("mul[(]\d+,\d+[)]",origLine)
#     for sett in commands:
#        for mul in sett:
#           factors = re.findall("\d+",mul)
#           thesum += int(factors[0]) * int(factors[1])

#     for nsett in notCommands:
#        for nmul in nsett:
#           factors = re.findall("\d+",nmul)
#           thesum += int(factors[0]) * int(factors[1])


for mul in commands:
    factors = re.findall("\d+",mul)
    thesum += int(factors[0]) * int(factors[1])


print("Sum is ",thesum)
#141,441,084 current no filter but going through logic
#170,807,108 correct all
