class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        indexT = indexS = 0
        while indexT < len(t) and indexS < len(s):
            if s[indexS] == t[indexT]:
                indexT += 1
            indexS += 1
        return len(t) - indexT