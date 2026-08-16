class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_prods = []
        prev = 1

        for num in nums:
            prod = prev * num
            # print(f"prev = {prev} | prod = {prod}")
            prev = prod
            prefix_prods.append(prod)

        # print(prefix_prods)

        postfix_prods = [1] * len(nums) # intialize an n length array
        prev = 1
        for i, num in enumerate(nums[::-1]):
            
            prod = prev*num
            # print(f"i = {i} | prev = {prev} | prod = {prod}")
            postfix_prods[(len(nums)-1-i)] = prod
            prev = prod

        # print(postfix_prods)

        output_arr = []

        for i in range (0,len(nums)):

            if i == 0:
                # no left
                output_arr.append(postfix_prods[1])

            elif i == (len(nums)-1):
                # no right
                output_arr.append(prefix_prods[len(nums)-2])

            else:
                output_arr.append(prefix_prods[i-1]*postfix_prods[i+1])
        
        # print(output_arr)
        return output_arr