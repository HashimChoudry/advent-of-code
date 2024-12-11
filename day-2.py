def isSafeHelper(arr):
    canBool = False
    if(isSafe(arr)):
        return True
    else:
        for i in range(len(arr)):
            # Create a new array excluding the element at index i
            modified_array = arr[:i] + arr[i+1:]
            if(isSafe(modified_array)):
                canBool = True
        return canBool

def isSafe(arr):
    increaseBool = False
    decreaseBool = False
    rangeBool = False
    for i in range(len(arr) - 1):
        if(arr[i] > arr[i+1]):
            decreaseBool = True
        else:
            decreaseBool = False
            break
    
    for j in range(len(arr) - 1):
        if(arr[j] < arr[j+1]):
            increaseBool = True
        else:
            increaseBool = False
            break

    for k in range(len(arr) -1):
        if (abs(arr[k]-arr[k+1])<=3) and (abs(arr[k]-arr[k+1])>0):
            rangeBool=True
        else:
            rangeBool = False
            break
    
    
    if (decreaseBool or increaseBool) and rangeBool:
        return True
    else:
        return False 

if __name__ == "__main__":
    safeNum = 0
    tst = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]
    file_path = "data-day2.txt"  

    with open(file_path, "r") as file:
        for line in file:
            # Convert line into a list of integers
            numbers = list(map(int, line.split()))
            
            # Perform the safety check
            if (isSafeHelper(numbers)):
                safeNum += 1
    print(safeNum)
        