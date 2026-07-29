class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num not in counter.keys():
                counter[num] = 1
                # print(f"First occurrence of {num}")
            else:
                counter[num]+=1
                # print(f"More than first occurence of {num}")

        # print(f"Final Counter: {counter}")
        for val in counter.values():
            if val >1:
                return True

        return False # this is how it should be