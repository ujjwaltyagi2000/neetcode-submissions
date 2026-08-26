class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # handle edge case first where nums is empty --> longest sequence length = 0
        if not nums:
            return 0

        nums.sort()
        print(nums)
        longest = 1
        current_streak = 1

        for i in range(1,len(nums)):
            
            # if consecutive, increase streak
            if nums[i] == nums[i-1] + 1:
                current_streak+=1
            
            # don't do anything for duplicates
            elif nums[i] == nums[i-1]:
                continue

            else:
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest,current_streak)