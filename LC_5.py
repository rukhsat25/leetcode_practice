def expand(s,start,end):
    while start>=0 and end<len(s) and s[start]==s[end]:
        start-=1
        end+=1
    
    return s[start+1:end]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest=''
        for i in range(len(s)):
            odd_palin=expand(s,i,i)
            even_palin=expand(s,i,i+1)
            if len(longest)<max(len(odd_palin),len(even_palin)):
                longest=max([odd_palin,even_palin],key=len)
        return longest
