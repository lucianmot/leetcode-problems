// Python - 344. Reverse String
// https://leetcode.com/problems/reverse-string/submissions/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        x = 0
        if len(s) % 2 == 0:
            y = int(len(s)/2)
        else:
            y = int((len(s)-1)/2)
        for i in range(0, y, 1):
            x = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = x
        # s.reverse()
        
