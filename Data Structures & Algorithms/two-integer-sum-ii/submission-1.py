
# Using Hash Maps
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         comp_map = {}

#         for i,num in enumerate(numbers):

#             compliment = target - num
#             if compliment not in comp_map:
#                 comp_map[num] = i+1
            
#             elif compliment in comp_map:
#                 print("valid pair:")
#                 print(comp_map[compliment], num)
#                 return [comp_map[compliment], i+1]
    
#         print(comp_map)

# Using Two Pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            sum = numbers[left] + numbers[right]
            # print(f"Sum = {sum}")

            if sum < target: 
                left += 1
                # print(f"Moving left to the right")

            elif sum > target:
                right -= 1
                # print(f"Moving right to the left")

            elif sum==target:
                # print(f"Found the valid pair")
                return [left+1,right+1]

        return False











