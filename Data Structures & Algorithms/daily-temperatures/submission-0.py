class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = []
        st = []
        j = len(temperatures) - 1

        while j >= 0:
            result_val = 0
            while len(st) > 0:
                if temperatures[j] >= temperatures[st[-1]]:
                    st.pop()
                else:
                    result_val = st[-1] - j
                    break
            result.insert(0, result_val)
            st.append(j)
            j -= 1
        
        return result

            
                    

