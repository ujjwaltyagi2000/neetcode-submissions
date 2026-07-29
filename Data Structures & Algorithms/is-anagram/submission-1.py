class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count characters in a string for both
        # if both counts are same --> anagram, else false

        # is_anagram --> true, not_anagram --> false
        s_counter = {} # counting frequency of characters in string s
        t_counter = {} # counting frequency of characters in string t

        for char in s:
            if char not in s_counter:
                s_counter[char] = 1
            else:
                s_counter[char] += 1
        
        # print(f"S-counter: {s_counter}")

        for new_char in t:
            if new_char not in t_counter:
                t_counter[new_char] = 1
            else:
                t_counter[new_char] += 1

        # print(f"T-counter: {t_counter}")

        if s_counter == t_counter:
            # print("S and T are anagrams")
            return True
        else:
            # print("NOT ANAGRAMS")
            return False