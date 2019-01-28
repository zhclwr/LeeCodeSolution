class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x >= 0:
        	s = str(x)
        else :
        	flag = True
        	s = str(x)[1:]
        temp = int(s[::-1])
        if temp > 2147483647:
        	return 0
        if flag:
        	result = 0 - temp
        else: 
        	result = temp

        print(result)
        return result


Solution().reverse(-15342369)