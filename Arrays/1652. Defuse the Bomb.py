class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        elif k > 0:
            tsum = sum(code)
            temp = code[:]
            for i in range(n):
                s = tsum
                if i == 0 :
                    tempValue = 0
                    for j in range(k):
                        tempValue+=temp[j+1]
                    code[i] = tempValue
                else:
                    if(i<n):
                        tempValue = i+k
                        if(tempValue >= n):
                            tempValue -= n
                        code[i] = code[i-1] - temp[i] + temp[tempValue]
            return code
        else:
            tsum = sum(code)
            temp = code[:]
            for i in range(n):
                s = tsum
                if i == 0 :
                    tempValue = 0
                    for j in range(n-1,n-1+(k),-1):
                        tempValue+=temp[j]
                    code[i] = tempValue
                else:
                    if(i<n):
                        tempValue = i+k
                        if(tempValue <= 0):
                            tempValue = n - 1 + tempValue
                        else:
                            tempValue -=1
                        # print(i,":",tempValue, code[i-1],temp[tempValue])
                        code[i] = code[i-1] + temp[i-1] - temp[tempValue]
            return code



        