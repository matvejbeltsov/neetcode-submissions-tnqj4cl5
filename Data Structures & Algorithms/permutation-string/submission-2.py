class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        dict_s = Counter(s1)
        count_window = dict()

        for right in range(len(s2)):
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1

            if (right - left + 1) > len(s1):
                count_window[s2[left]] -= 1

                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left += 1
            
            if dict_s == count_window:
                return True
        return False

        