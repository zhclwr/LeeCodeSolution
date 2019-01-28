class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        temp = ''
        temp_num = 0
        for i in s:
            if i not in temp:
                temp += i
                temp_num += 1
            else:
                if num < temp_num:
                    num = temp_num
                index = temp.index(i)
                temp = temp[(index+1):] + i
                temp_num = len(temp)
        if temp_num > num:
            num = temp_num
        return num


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcaaabcbb"))
