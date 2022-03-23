#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        #code here
        if(A>B and A>C):
            return max(B,C)
        if(B>A and B>C):
            return max(A,C)
        if(C>A and C>B):
            return max(A,B)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends
