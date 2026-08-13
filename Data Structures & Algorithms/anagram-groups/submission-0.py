class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}
        
        for text in strs:
            
            # split string into characters: cat = ['c','a','t']
            chars = list(text)

            # if two words are anagrams, their characters after sorting would be same
            # example: act and cat -> ['a','c','t']
            # therefore we sort the characters
            chars.sort()

            # dictionary key cannot be a list, so we convert this list into a string and set as a key
            # this combined string will be same for all anagram words
            chars = "".join(chars)

            # objective-->
            # {
            #     "act"  = ["act", "cat"]
            # }

            # print(chars)

            # if key doesn't exist, create it and initialize an array with current text 
            if chars not in map:
                map[chars] = []
                map[chars].append(text)

            # if key already exists
            else:
                map[chars].append(text)

        anagrams = []

        # iterate through values of above hash map and append into a single array
        for val in map.values():

            anagrams.append(val)

        # print(anagrams)
        return anagrams






