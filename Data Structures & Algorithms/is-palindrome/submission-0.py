class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1

        while left < right:

            print(f"left = {left}-->{s[left]} | right = {right}-->{s[right]}")

            if not s[left].isalnum():
                print(f"Character {s[left]} is not alphamumeric, shifting left") 
                left += 1
                continue
            
            if not s[right].isalnum():
                print(f"Character {s[right]} is not alphamumeric, shifting right") 
                right -= 1
                continue
            
            elif s[left].lower() != s[right].lower():
                print(f"String is not a palindrome")
                return False

            left+=1
            right-=1

        return True