with open("data-day4.txt","r") as file:
    word_grid = file.read().strip().split("\n")

n = len(word_grid)
m = len(word_grid[0])


directions = []
for x in range(-1,2):
    for y in range(-1,2):
        if(x !=0 or y != 0):
            directions.append((x,y))


def wordFound(x,y,direction):
    xDirection,yDirection = direction;
    for k,l in enumerate('XMAS'):
        nextX = x+k * xDirection
        nextY = y +k *yDirection
        if not (0<=nextX < n and 0<=nextY < m):
            return False
        if word_grid[nextX][nextY] != l:
            return False
    return True

def newWordFound(x,y):
    if not (1<=x < n -1and 1<=y < m -1):
        return False
    if word_grid[x][y] != 'A':
        return False
    
    diagonal1 = f"{word_grid[x-1][y+1]}{word_grid[x+1][y-1]}"
    diagonal2 = f"{word_grid[x+1][y+1]}{word_grid[x-1][y-1]}"
    if diagonal1 in ["SM",'MS'] and diagonal2 in ["SM","MS"]:
        print (diagonal1,diagonal2)
        return True
    return False

    


ans = 0
for i in range(len(word_grid)):
    for j in range(len(word_grid[0])):
          ans += newWordFound(i,j)

print(ans)
    

                

