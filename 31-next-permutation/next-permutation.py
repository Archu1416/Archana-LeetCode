class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                f=i
                break
        else:
            nums.reverse()
            return nums
        s=0
        for i in range(len(nums)-1,f,-1):
            if nums[i]>nums[f]:
                s=i
                break
        nums[s],nums[f]=nums[f],nums[s]
        nums[f+1:]=reversed(nums[f+1:])
        return nums