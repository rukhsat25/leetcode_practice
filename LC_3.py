from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=defaultdict(int)
        m=0
        t=""
        if len(s)==0:
            return 0
        for i in range(len(s)):
            if s[i] in t:
                m=max(m,len(t))
                t=s[d[s[i]]+1:i+1]
                d[s[i]]=i
            else:
                t+=s[i]
                d[s[i]]=i
        return max(m,len(t))
