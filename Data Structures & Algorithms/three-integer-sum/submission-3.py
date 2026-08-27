class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)

        nums.sort()
        print(nums)
        arrs = []

        for i in range (0, length - 2):

            target = -nums[i]
            left = i+1 
            right = len(nums)-1

            # print(f"A = {nums[i]}, B + C = {target} | left = {left} | right = {right}")

            if i>0 and nums[i]==nums[i-1]:
                continue

            while left<right:

                # print(f"While loop for {i}th element --> {nums[i]} | left = {left} right = {right}")
                
                if nums[left]+nums[right]==target :
                    # print(f"Found valid pair: {nums[left]}, {nums[right]} for element nums[{i}] --> {nums[i]}")
             
                    arrs.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif nums[left]+nums[right]<target:
                    left+=1

                elif nums[left]+nums[right]>target:
                    right-=1

        return arrs