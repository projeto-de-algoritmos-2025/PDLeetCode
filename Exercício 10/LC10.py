class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        curr = [False] * (n + 1)
    
        prev[0] = True
        for j in range(2, n + 1):
            if p[j-1] == '*':
                prev[j] = prev[j-2]
    
        for i in range(1, m + 1):
            curr[0] = False
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    curr[j] = curr[j-2] or (
                        prev[j] and (p[j-2] == s[i-1] or p[j-2] == '.')
                    )
                else:
                    curr[j] = prev[j-1] and (p[j-1] == s[i-1] or p[j-1] == '.')
        
            prev, curr = curr, [False] * (n + 1)
    
        return prev[n]
