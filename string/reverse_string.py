class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words=S.split('.')
        reverse=words[::-1]
        reverse_string='.'.join(reverse)
        return reverse_string
        
        
sol = Solution() 
S=('pqr.mno')
result=sol.reverseWords(S)
print(result)