class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
            
        char_to_word = {}
        word_set = set()
        for i in range(len(s)):
            char = pattern[i]
            word = s[i]
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_set and char not in char_to_word:
                return False
            word_set.add(word)
            char_to_word[char] = word 

        return True
