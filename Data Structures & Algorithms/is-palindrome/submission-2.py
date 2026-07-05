class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            if s[lp].isalnum() == False:
                lp += 1
                continue

            if s[rp].isalnum() == False:
                rp -= 1
                continue

            if s[lp].lower() != s[rp].lower():
                return False
            
            lp += 1
            rp -= 1
        
        return True