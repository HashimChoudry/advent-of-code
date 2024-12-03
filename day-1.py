leftArr = [3,1,2,4,3,3]
rightArr = [4,3,5,3,9,3]

def merge(arr,left,middle,right):
    leftLen = middle - left + 1
    rightLen = right-middle

    leftArr = [0] * leftLen
    rightArr = [0] * rightLen


    for i in range(leftLen):
        leftArr[i] = arr[left +i]
    for j in range(rightLen):
        rightArr[j] = arr[middle+ 1 + j]
    i=0
    j=0
    k=left
    while i<leftLen and j < rightLen:
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i+=1
        else:
            arr[k] = rightArr[j]
            j+=1
        k+=1
    
    while i<leftLen:
        arr[k] = leftArr[i]
        i+=1
        k+=1
    while j< rightLen:
        arr[k] = rightArr[j]
        j+=1
        k+=1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left+right) // 2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

if __name__ == "__main__":
    arr1 = []
    arr2 = []

    leftArr = [3,4,2,1,3,3]
    rightArr = [4,3,5,3,9,3]

    similarity = {}

    sum = 0

    with open('data.txt','r') as file:
        for line in file:
            num1,num2 = map(int,line.split())
            arr1.append(num1)
            arr2.append(num2)

    for i in range(len(arr1)):
        if arr1[i] not in similarity:
            counter = 0
            for j in range(len(arr2)):
                if(arr2[j] == arr1[i]):
                    counter +=1
            similarity[arr1[i]] = arr1[i] * counter
    
    for num in arr1:
        sum += similarity[num]
            
    print(sum)
    # with open('data.txt','r') as file:
    #     for line in file:
    #         num1,num2 = map(int,line.split())
    #         arr1.append(num1)
    #         arr2.append(num2)
    

    # mergeSort(arr1,0,len(arr1) - 1)
    # mergeSort(arr2,0,len(arr2) - 1)

    # sum = 0
    # for i in range(len(arr1)):
    #     sum += abs(arr1[i] - arr2[i])
        
    
    
    
    