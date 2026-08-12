class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}

        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in nums[i+1:]: 
                elem1 = i
                elem2 = nums.index(compliment,i+1) # start searching from i+1
                return [elem1, elem2]