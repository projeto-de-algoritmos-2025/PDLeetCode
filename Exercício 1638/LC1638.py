from functools import lru_cache

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # Calcula o número de substrings em 's' que diferem de alguma substring em 't' por no máximo um caractere, usando recursão com memoização (DP top-down).
        n, m = len(s), len(t)
        total_count = 0

        @lru_cache(None) # @lru_cache(None) cria um cache para memoizar os resultados da função. É a forma padrão de fazer memoização em Python.

        # Função recursiva que calcula o comprimento do sufixo IDÊNTICO.
        def get_len_suffixo(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            
            # Se os caracteres forem iguais: estendemos o sufixo idêntico.
            if s[i] == t[j]:
                return 1 + get_len_suffixo(i - 1, j - 1)
            
            # Se forem diferentes: a sequência de caracteres idêncitos é quebrada.
            return 0

        @lru_cache(None)
        # Função recursiva que conta o número de substrings com UMA DIFERENÇA.
        def count_diff(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0

            if s[i] == t[j]:
                return count_diff(i - 1, j - 1) # Se os caracteres são iguais, eles não introduzem uma nova diferença.

            else:
                # Se os caracteres são diferentes, cria a diferença. O número de substrings é (1 + o comprimento do sufixo idêntico).
                return 1 + get_len_suffixo(i - 1, j - 1)

        # A resposta é a soma das contagens de substrings com no máx. 1 diferença.
        for i in range(n):
            for j in range(m):
                total_count += count_diff(i, j)
                
        return total_count