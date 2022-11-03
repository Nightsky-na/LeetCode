class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            score_left = [i == str(0) for i in left]
            score_right = [i == str(1) for i in right]
            if sum(score_left)+sum(score_right) > max_score:
                max_score = sum(score_left)+sum(score_right)
            
        return max_score
            
            