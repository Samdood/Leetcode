class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie["is_word"] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        def dfs(index, trie) -> bool:
            nonlocal word
            if index == len(word) and "is_word" in trie:
                return True
            if index >= len(word):
                return False

            char = word[index]
            if char in trie:
                return dfs(index + 1, trie[char])
            if char != ".":
                return False
            for c in trie.keys():
                if c == "is_word":
                    continue
                if dfs(index + 1, trie[c]):
                    return True
            return False

        return dfs(0, trie)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)