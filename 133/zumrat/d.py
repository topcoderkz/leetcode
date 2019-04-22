class StreamChecker:
    def __init__(self, words: List[str]):
        self.w = collections.Counter(words)
        self.q = []
        self.suffix = collections.defaultdict(bool)
        for word in words:
            s = ""
            for i in range(len(word) - 1, -1, -1):
                s += word[i]
                self.suffix[s[::-1]] = True
            
    def query(self, letter: str) -> bool:
        self.q.append(letter)
        s = ""
        for i in range(len(self.q) - 1, -1, -1):
            s += self.q[i]
            if s[::-1] in self.w:
                return True
            if s[::-1] not in self.suffix:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
