class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while (nums[i] + nums[j] != target):
            if (j == len(nums) - 1):
                i += 1
                j = i + 1
            else:
                j += 1

        return [i,j]