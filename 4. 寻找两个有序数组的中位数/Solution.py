class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        for i in range(len(nums) - 1):
        	for j in range(i + 1, len(nums)):
        		if nums[i] > nums[j]:
        			temp = nums[i]
        			nums[i] = nums[j]
        			nums[j] = temp
        print(nums)
        if len(nums) % 2 == 1:
            return nums[int((len(nums) +1 ) / 2) - 1]
        else:
            mid = int(len(nums) / 2)
            return (nums[mid] + nums[mid - 1]) / 2

Solution().findMedianSortedArrays([1,8,5], [4,3,2])