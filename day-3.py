import re

with open("data-day3.txt", "r") as file:
    line = file.read().strip()


correct =re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))",line)

flag = True
ans = 0

for thing in correct:
    if thing[2] == "" and flag:
        ans+= int(thing[0]) * int(thing[1])
    else:
        if thing[2] == "do()":
            flag = True
        else:
            flag = False

print(ans)
