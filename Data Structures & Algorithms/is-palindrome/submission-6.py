class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        lenght = len(s)
        middle = round(lenght/2)
        for index in range(0,middle):
            if s[index] != s[len(s) - 1 - index]: 
                return False

        return True


        