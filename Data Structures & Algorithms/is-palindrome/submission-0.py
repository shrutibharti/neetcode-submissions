class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(filter(str.isalnum,s))
        s=s.lower()
        new_s=s[::-1] # make them in lower format
        if s==new_s:
            return True
        return False
        