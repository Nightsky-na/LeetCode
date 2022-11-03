class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_ans = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0: 
                list_ans.append("FizzBuzz")
            elif i % 3 == 0:
                list_ans.append("Fizz")
            elif i % 5 == 0:
                list_ans.append("Buzz")
            else: 
                list_ans.append(str(i))
                
            
        return list_ans