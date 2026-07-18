class Solution:
    def isValid(self, s: str) -> bool:

        brac_list = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for i in range(len(s)):
            if s[i] not in brac_list:
                stack.append(s[i])
            else:
                if len(stack) != 0 and stack[-1] == brac_list[s[i]]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True 
        else: 
            return False
                