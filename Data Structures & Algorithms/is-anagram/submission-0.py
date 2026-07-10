class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        my_dict_1 = {}
        my_dict_2 = {}

        for i in range(len(s)):
            if(s[i] in my_dict_1):
                my_dict_1[s[i]] = my_dict_1[s[i]] + 1
            else:
                my_dict_1[s[i]] = 1
            
        for i in range(len(t)):
            if(t[i] in my_dict_2):
                my_dict_2[t[i]] = my_dict_2[t[i]] + 1
            else:
                my_dict_2[t[i]] = 1

        return my_dict_1 == my_dict_2

 

        