'''
    {
        a : {
            p :{
                p : ..., 
                is_word : True
            }
        }
    }

'''

class Trie:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        trie = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

        if "is_word" not in trie:
            trie["is_word"] = True

    def search(self, word: str) -> bool:
        trie = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in trie:
                return False
            trie = trie[char]
        return "is_word" in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)