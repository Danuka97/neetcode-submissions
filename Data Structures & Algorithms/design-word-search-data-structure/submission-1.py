class WordDictionary:

    def __init__(self):
        self.childern = {}
        self.is_end = False
        

    def addWord(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.childern:
                node.childern[char] = WordDictionary()
            node = node.childern[char]
        node.is_end = True

    

        

    def search(self, word: str) -> bool:

        def dfs(i,node):

            if i == len(word):
                return node.is_end

            char = word[i]

            if char != ".":
                if char not in node.childern:
                    return False
                return dfs(i+1,node.childern[char])
            else:
                for child in node.childern.values():
                    if dfs(i+1,child):
                        return True
                return False

        return dfs(0,self)


        
