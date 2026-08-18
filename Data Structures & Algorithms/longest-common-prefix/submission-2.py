class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        first_word = strs[0]
        longest_prefix = []
        for i, char in enumerate(first_word):
            mismatch = False
            for word in strs:
                if len(word)>i and word[i] == char:
                    continue
                    # longest_prefix.append(char)
                else:
                    mismatch = True
                    break

            if mismatch:
                break

            longest_prefix.append(char)

        longest_prefix_str = "".join(longest_prefix)
        # print(longest_prefix_str)
        return longest_prefix_str