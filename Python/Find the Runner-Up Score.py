if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    count = -1
    runnerup = arr[-1]
    
    for x in range(n):
        if arr[count] == arr[-1]:
            count = count - 1
        else:
            runnerup = arr[count]
            
    print (runnerup)