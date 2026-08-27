class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {v: i for i, v in enumerate(nums)} 
        for i, num in enumerate(nums):
            value = target - num
            if ( value in d.keys()):
                j = d.get(value, 0)
                if ( i != j):
                    return [i, j]