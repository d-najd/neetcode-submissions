class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            left_char = s[lp].lower()
            right_char = s[rp].lower()

            if left_char.isalnum() == False:
                lp += 1
                continue

            if right_char.isalnum() == False:
                rp -= 1
                continue

            if left_char != right_char:
                return False
            
            lp += 1
            rp -= 1
        
        return True