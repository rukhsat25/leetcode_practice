//code by Utkarsh
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=[[] for _ in range(numRows)]
        j=0
        k=numRows-2
        if k==-1:
            return s
        for i in range(len(s)):
            if j<numRows:
                l[j].append(s[i])
                j+=1
                if j==numRows:
                    k=numRows-2
            elif k>=0:
                l[k].append(s[i])
                k-=1
                if k==-1:
                    j=1
        answer=""
        for i in l:
            answer+="".join(i)
        return answer
