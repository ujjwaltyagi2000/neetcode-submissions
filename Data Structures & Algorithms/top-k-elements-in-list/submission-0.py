class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_map = {}

        # create a hashmap of nums and frequencies
        for num in nums:

            if num not in nums_map:
                nums_map[num] = 1
            
            else:
                nums_map[num] += 1

        # sort and return first k elements with highest frequencies
        frequency_tuples = [(key, value) for key, value in nums_map.items()]
        # print(frequency_tuples)

        # sort this on 2nd element
        frequency_tuples.sort(key=lambda x:x[1], reverse=True)
        
        # fetch first values from all tuples
        frequent_elements = [x[0] for x in frequency_tuples]

        return frequent_elements[:k]

        
            