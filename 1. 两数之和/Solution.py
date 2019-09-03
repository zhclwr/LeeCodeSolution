from Lib.typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while nums[i] + nums[j] != target:
            if j < len(nums) - 1:
                j += 1
            else:
                i += 1
                j = i + 1
        return [i, j]


if __name__ == '__main__':
    s = Solution()
    res = s.twoSum([2, 7, 11, 15], 26)
    print(res)
