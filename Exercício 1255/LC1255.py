import collections
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        # Frequência das letras = capacidade da mochila
        letter_counts = collections.Counter(letters)
        # Num de palavras = quantidade de itens na mochila
        n = len(words)

        def backtrack(index: int) -> int:
            if index == n:
                return 0

            score_pulou_palavra = backtrack(index + 1)

            current_word = words[index]
            current_word_score = 0
            can_form_word = True
            
            # Frequência de letras necessárias p/ palavra atual
            word_counts = collections.Counter(current_word)
            
            for char, count_needed in word_counts.items():
                if letter_counts[char] < count_needed:
                    can_form_word = False
                    break # verifica se tem letra suficiente p/ formar a palavra
            
            score_pegou_palavra = 0
            if can_form_word:
                for char, count_needed in word_counts.items():
                    current_word_score += score[ord(char) - ord('a')] * count_needed
                
                # Remove letras usadas do conjunto de letras disponíveis
                for char, count_needed in word_counts.items():
                    letter_counts[char] -= count_needed
                
                score_pegou_palavra = current_word_score + backtrack(index + 1)
                
                # Devolve letras usadas para o backtracking
                for char, count_needed in word_counts.items():
                    letter_counts[char] += count_needed

            return max(score_pulou_palavra, score_pegou_palavra)

        return backtrack(0)