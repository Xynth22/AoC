import math

def swap(a,old,new):
    temp = a[new]
    a[new]=a[old]
    a[old]=temp
    return a

def middle_print(p,r):
    passing = True
    for rule in ruleSet:
        if (rule[0] in p) and (rule[1] in p):
            if p.index(rule[0]) > p.index(rule[1]):
                passing = False
    if passing:
        return p[math.floor(len(p)/2)]
    else:
        return 0


def fixed_middle(p,r):
    passing = False
    while (not passing):
        passing = True
        for rule in ruleSet:
            if (rule[0] in p) and (rule[1] in p):
                if p.index(rule[0]) > p.index(rule[1]):
                    passing=False
                    p=swap(p,p.index(rule[0]),p.index(rule[1]))
                    # if p.index(rule[0]) == (len(p)-1):
                    #     p = swap(p,p.index(rule[0]),0)
                    # else:
                    #     p = swap(p,p.index(rule[0]), p.index(rule[0]) - 1)
    return p[math.floor(len(p)/2)]


                 

#with open("test.txt", "r") as file:
with open("input_day5_p1.txt", "r") as file:
    first_section, second_section = file.read().split('\n\n')
rules = first_section.strip().split('\n')
pagesets = second_section.strip().split('\n')

goodSum=0
badSum = 0
ruleSet =[]
for rule in rules:
    ruleSet.append(list(map(int,rule.split('|'))))

for set in pagesets:
    pages = list(map(int,set.split(',')))
    mid = middle_print(pages,ruleSet)
    goodSum += mid
    if mid == 0:
        correctedMid = fixed_middle(pages,ruleSet)
        badSum += correctedMid
    


print(goodSum)
print(badSum)