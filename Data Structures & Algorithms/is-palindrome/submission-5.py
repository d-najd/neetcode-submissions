class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            left_char = s[lp]
            right_char = s[rp]

            if left_char.isalnum() == False:
                lp += 1
                continue

            if right_char.isalnum() == False:
                rp -= 1
                continue

            if left_char.lower() != right_char.lower():
                return False
            
            lp += 1
            rp -= 1
        
        return True