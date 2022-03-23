def binarySearch(arr,low,high):
    for i in range(len(arr)):
        if arr[i]==i:
            return i
    return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        print(binarySearch(arr,0,n-1))
# } Driver Code Ends
