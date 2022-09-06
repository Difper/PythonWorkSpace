def MathChallenge(arr):
    i=0
    list = []
    while(i < len(arr)):
        j=i
        temp =  arr[i]
        while(j>=0):
            if(arr[j] < arr[i]):
                temp = arr[j]
                break
            j = j-1
        if(arr[i]== temp):
            list.append(-1)
        else:
            list.append(temp)
        i = i+1
        
    return list
print(MathChallenge([5,2,3,6,9,5,3]))