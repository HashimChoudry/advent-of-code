rules = []
with open("data-day5-keys.txt","r") as file:
    for line in file:
        rules.append(line.strip().split('|'))

data = []
with open("data-day5-data.txt","r") as file:
    data = [list(map(int, line.split(','))) for line in file]

def isAllowed(arr,rules):
    dict = {}
    for i in range(len(arr)):
        if not(arr[i] in dict):
            dict[arr[i]] = i
    for j in rules:
        if(int(j[0]) in dict and int(j[1]) in dict):
            if dict[int(j[0])] > dict[int(j[1])]:
                return False
    return True

sum = 0

for x in data:
   if(isAllowed(x,rules)):
       mid = len(x)//2
       sum += x[mid]

print(sum)