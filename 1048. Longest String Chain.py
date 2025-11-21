class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_index = {}
        dp = {}
        for i,w in enumerate(words):
            word_index[w]=i
        def dfs(i):
            if i in dp:
                return dp[i]
            w = words[i]
            res = 1
            for j in range(len(w)):
                pred = w[:j] + w[j+1:]
                if pred in word_index:
                    res = max(res, 1 + dfs(word_index[pred]))
            dp[i] = res
            return res
        for i in range(len(words)-1, -1 ,-1):
            dfs(i)
        return max(dp.values())