class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_map = {}
        size = len(nums)

        for num in nums:
            if num not in element_map:
                element_map[num] = 1

            elif num in element_map:
                element_map[num]+=1

        for key in element_map.keys():

            if element_map[key] > size/2:
                return key