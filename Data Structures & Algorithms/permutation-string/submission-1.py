class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = {}
        freq2 = {}

        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i], 0) + 1
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
        
        if freq1 == freq2:
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1

            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            
            left += 1

            if freq1 == freq2:
                return True

        return False