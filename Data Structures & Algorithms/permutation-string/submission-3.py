class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        dict_s1 = Counter(s1)

        count_window = {}

        for right in range(len(s2)):
            char = s2[right]
            count_window[char] = count_window.get(char, 0) + 1

            if (right - left + 1) > len(s1):
                count_window[s2[left]] -= 1
                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left += 1
            
            if dict_s1 == count_window:
                return True
        return False