class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        l, r = 0, len(nums) -1

        while l<r:
            mid = int((l + r)/2)

            #if nums[l] > nums[r]: #rotated
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
        
            # if nums[r]>nums[l]: #non rotated
            #     return nums[l]
        
        return nums[l]
        
        # 3,4,5,6,1,2
        # l = 0 ,3
        # r = 5 , 4
        # mid = 2 , 4, 3