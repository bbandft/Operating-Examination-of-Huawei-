class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word = set(words)
        sum = 0
        for i in words:
            for j in range(1,len(i)):
                word.discard(i[j:])
        for i in word:
            sum +=len(i)+1
        return sum