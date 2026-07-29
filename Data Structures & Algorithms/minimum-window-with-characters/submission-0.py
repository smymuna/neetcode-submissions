class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        res = [-1, -1]
        resLen = float("inf")
        countT = {}
        window = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        left = 0
        need = len(countT)
        have = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                # if freq2[s[left]] == 0:
                #     del freq2[s[left]]
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right + 1] if resLen != float("inf") else ""
            