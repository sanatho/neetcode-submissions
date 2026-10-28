class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {}

        for i, el in enumerate(nums):
            valMap.update({el:i})

        for i, el in enumerate(nums):
            targetVal = target - el

            if targetVal in valMap and i != valMap[targetVal]:
                return [i, valMap[targetVal]]