class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setEl = set()

        for el in nums:
            setEl.add(el)

        return len(nums) != len(setEl)