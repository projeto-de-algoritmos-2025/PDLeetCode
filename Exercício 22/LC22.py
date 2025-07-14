class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # dp[i] guarda as combinações para i pares
        dp: list[list[str]] = [[] for _ in range(n+1)]
        dp[0] = [""]  # Uma string vazia para zero pares

        for i in range(1, n+1):
            current: list[str] = []
            # c pares “dentro” e (i-1-c) pares “depois”
            for c in range(i):
                for left in dp[c]:
                    for right in dp[i-1-c]:
                        current.append(f"({left}){right}")
            dp[i] = current

        return dp[n]
