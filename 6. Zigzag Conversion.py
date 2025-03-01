class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        n = len(s)
        res =''
        for r in range(numRows):
            inc = 2*(numRows-1)
            for i in range(r,n,inc):
                res+= s[i]
                if(r>0 and r< numRows-1) and (i+ inc - 2*r)<n:
                    res+=s[i+ inc - 2*r]
        return res
                

            

        