class Solution:
    def isPalindrome(self, s: str) -> bool:

        combined_string = "".join(filter(str.isalnum, s))
        combined_string = combined_string.lower()

        i = 0
        j = len(combined_string) - 1

        while i <= j:
            print(combined_string[i], combined_string[j])
            if combined_string[i] != combined_string[j]:
                return False
            i += 1
            j -= 1
        return True