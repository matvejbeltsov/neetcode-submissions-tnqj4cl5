class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        count_window = {}
        left = 0
        res_right = float('inf')
        res_left = 0
        have = 0
        need = len(dict_t)

        for right in range(len(s)):
            count_window[s[right]] = count_window.get(s[right], 0) + 1

            if s[right] in dict_t and count_window[s[right]] == dict_t[s[right]]:
                have += 1
            

            while have == need:
                if (right - left + 1) < (res_right - res_left + 1):
                    res_left = left
                    res_right = right
                
                count_window[s[left]] -= 1

                if s[left] in dict_t and count_window[s[left]] < dict_t[s[left]]:
                    have -= 1
                
                left += 1
        
        return s[res_left:res_right + 1] if res_right != float('inf') else ""