
class Solution:
    def middle(self,A,B,C):
        #code here
        l=[]
        l.append(A)
        l.append(B)
        l.append(C)
        l.sort()
        if(l[0]<l[1] and l[1]<l[2]):
           return l[1]
        return 0

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
