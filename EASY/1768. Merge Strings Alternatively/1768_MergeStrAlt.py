class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        i = 0
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged_str += word1[i]
            if i < len(word2):
                merged_str += word2[i]
        return merged_str
