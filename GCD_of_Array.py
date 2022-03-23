# https://practice.geeksforgeeks.org/problems/gcd-of-array0614/1

class Solution:
    def gcd(self, n, arr):
        # code here 
        i=0
        res=arr[i]
        while(i<n):
            a=res    #0
            b=arr[i]  #1
            while(b): #2,4
                a,b=b,a%b
            res=a #gcd of 2,4
            i+=1 # i=2
        return res
         
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(n,arr))
# } Driver Code Ends
