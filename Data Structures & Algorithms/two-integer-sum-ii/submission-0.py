class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        comp_map = {}

        for i,num in enumerate(numbers):

            compliment = target - num
            if compliment not in comp_map:
                comp_map[num] = i+1
            
            elif compliment in comp_map:
                print("valid pair:")
                print(comp_map[compliment], num)
                return [comp_map[compliment], i+1]

        # print(comp_map)