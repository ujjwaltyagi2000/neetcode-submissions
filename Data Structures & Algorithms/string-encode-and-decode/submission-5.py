# class Solution:

#     def encode(self, strs: List[str]) -> str:
        
#         combined_string = "ö".join(strs)
#         # print(combined_string)
#         return combined_string

#     def decode(self, s: str) -> List[str]:

#         # if s == "":
#         #     return []
#         strings_array = s.split(sep="ö")
#         # print(strings_array)
#         return strings_array

"""
PROBLEM WITH ABOVE CODE:

Question said strs[i] contains any possible characters out of 256 valid ASCII characters

"-" (hyphen) is one of them

if one str is like "hello-world", our code will break

so we cannot just separate strings by a hyphen and call it a day

we need to make the encoding more informative, that tells us exactly 
where the word boundaries lie
"""

"""

New Encoding Strategy -->

strs = ["neet", "co#de"]

encoded string = 4#neet5#co#de

now when we try to decode it,
> we will start from 0th character 
> move until we hit a '#' 
> to the left of '#' will be length of string (let length = x)
> from '#' sign we move to the right until x characters --> that is our string
> append all such string in an array


"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # strs = ["we","say",":","yes","!@#$%^&*()"]
        encoded_string = ""
        for s in strs:
            s_len = len(s)
            encoded_string += f"{len(s)}#{s}"

        print(encoded_string)
        return encoded_string

    # ENCODE FUNCTION IS CORRECT

    # def decode(self, s: str) -> List[str]:   
        
    #     # s = "5#Hello5#World"
    #     len_s = len(s)
    #     print(f"length of input string:{len_s}")
    #     all_strings = []

    #     if len_s>0:
    #         i=1


    #         while i<len(s):
                
    #             if s[i] == "#":
    #                 string_length = int(s[i-1])
    #                 print(f"Length: {string_length}") 
    #                 first_char_index = i+1
    #                 last_char_index = first_char_index + string_length
    #                 string = s[first_char_index:last_char_index]
    #                 print(f"String: {string}")
    #                 all_strings.append(string)
    #                 print(i)

    #             i+=string_length+2

    #         # print(all_strings)
    #         return all_strings

    #     else:
    #         return []

    """
    PROBLEM WITH ABOVE DECODE FUNCTION

    It assumes all length are SINGLE DIGITS!!

    If we 10#<string>
    it will only consider 0

    we need to use a while loop to traverse until next "#"
    """

    def decode(self, s: str) -> List[str]:   

        result = []
        i = 0 # pointer to traverse the string

        # traverse the entire string
        while i<len(s):
            
            # print(f"i = {i}")
            # pointer to move till the next "#"
            j=i
            
            while s[j] != "#":
                # move until hash is detected (1,2,3 digit length doesn't matter)
                j+=1
            
            print(f"i = {i} | j = {j}")
            length_str = s[i:j]
            length = int(length_str)

            print(f"Length: {length}")

            word_start = j+1
            word_end = word_start + length
            print(f"Start = {word_start} | End = {word_end}")

            word = s[word_start:word_end]
            result.append(word)
            
            i = word_end

        return result


