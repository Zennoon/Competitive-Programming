class Solution:
    def sortSentence(self, s: str) -> str:
        sortedList = []
        words = s.split(" ")
        for i in range(1, len(words) + 1):
            for word in words:
                if str(i) in word:
                    sortedList.append(word.replace(str(i), ""))
        return " ".join(word for word in sortedList)
