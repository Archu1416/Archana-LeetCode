class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=[(num,i) for i,num in enumerate(nums)]
        nums.sort()
        l=0
        r=len(nums)-1
        while l!=r:
            if nums[l][0]+nums[r][0]<target:
                l+=1
            elif nums[l][0]+nums[r][0]>target:
                r-=1
            else:
                return [nums[l][1],nums[r][1]]