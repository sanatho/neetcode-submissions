class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)

        if len(sortedT) != len(sortedS):
            return False

        for index in range(len(sortedS)):
            if sortedS[index] != sortedT[index]:
                return False
        
        return True
        