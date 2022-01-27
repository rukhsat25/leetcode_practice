class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1=len(text1)
        s2=len(text2)
        if s1==0 or s2==0:
            return 0
        dp=[]
        for i in range(s1+1):
            dp.append([0 for j in range(s2+1)])
        for i in range(s1):
            for j in range(s2):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[s1][s2]
