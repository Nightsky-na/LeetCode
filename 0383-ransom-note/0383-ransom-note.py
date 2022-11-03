class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        list_ans = []
        for i in ransomNote:
            if i in magazine:
                list_ans.append(True)
                index = magazine.index(i)
                magazine.pop(index)
        return sum(list_ans) == len(ransomNote)
        