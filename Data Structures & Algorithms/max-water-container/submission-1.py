class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # heights = [2,2,2]
        left = 0 
        right = len(heights) - 1
        print(left)
        print(right)
        max_area = 0

        print(heights)

        while left < right:
            width = (right - left) 

            if heights[left]<heights[right]:
                # print("Moving left pointer")
                height = min(heights[left], heights[right])
                # print(f"left = {left} --> {heights[left]} | right = {right} --> {heights[right]} | width = {width} | height = {height} | area = {width*height}")
                max_area = max(max_area, height*width)
                left += 1

            elif heights[right] < heights[left]:
                # print("moving right pointer")
                height = min(heights[left], heights[right])
                # print(f"left = {left} --> {heights[left]} | right = {right} --> {heights[right]} | width = {width} | height = {height} | area = {width*height}")
                right -= 1
                max_area = max(max_area, height*width)

            else:
                # print("moving both pointers")
                height = min(heights[left], heights[right])
                max_area = max(max_area, height*width)
                # print(f"left = {left} --> {heights[left]} | right = {right} --> {heights[right]} | width = {width} | height = {height} | area = {width*height}")
                left+=1
                right-=1

        # print(f"MAX AREA = {max_area}")
        return max_area




        