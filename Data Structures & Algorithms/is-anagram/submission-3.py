# METHOD 1 --> Character Frequency count and compare

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # count characters in a string for both
#         # if both counts are same --> anagram, else false

#         # is_anagram --> true, not_anagram --> false
#         s_counter = {} # counting frequency of characters in string s
#         t_counter = {} # counting frequency of characters in string t

#         for char in s:
#             if char not in s_counter:
#                 s_counter[char] = 1
#             else:
#                 s_counter[char] += 1
        
#         # print(f"S-counter: {s_counter}")

#         for new_char in t:
#             if new_char not in t_counter:
#                 t_counter[new_char] = 1
#             else:
#                 t_counter[new_char] += 1

#         # print(f"T-counter: {t_counter}")

#         if s_counter == t_counter:
#             # print("S and T are anagrams")
#             return True
#         else:
#             # print("NOT ANAGRAMS")
#             return False

#METHOD 2 --> Sort characters and compare

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for char in s:
            s_list.append(char)
        for new_char in t:
            t_list.append(new_char)

        # print(f"S list: {s_list}")
        # print(f"T list: {t_list}")

        s_list.sort()
        t_list.sort()

        # print(f"After Sorting:")
        # print(f"S list: {s_list}")
        # print(f"T list: {t_list}")

        if s_list == t_list:
            # print(f"ANAGRAMS")
            return True
        else:
            # print("NOT ANAGRAMS")
            return False